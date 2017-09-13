#Problem 0010 - Summation of Primes
#===============================================================================
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

#Answer: 
#First Version Time:  Seconds Per 1 iterations
#Second Version Time:  Seconds Per 1 iterations
#===============================================================================

from timeit import default_timer as timer

def main():
    loops = 1

    start = timer()
    for a in range (0, loops):
        result = problem()
    end = timer()

    print(result)
    print(str((end - start)) + " seconds") 

def problem():
    num_list = list(range(3, 2000001, 2))
    multiplier = 2
    print(num_list)

    for n in num_list:
        while n * multiplier < 2000000:
            if n * multiplier in num_list:
                num_list[(n * multiplier)-2] = 0
                #num_list.remove(n * multiplier)
            multiplier += 1
        multiplier = 2
        print(num_list)

    return sum(num_list + 2)

main()