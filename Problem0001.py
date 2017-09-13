#Problem 0001 - Multiples of 3 and 5
#===============================================================================
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#Answer: 233168
#Time: 0.8832 Seconds Per 10,000 iterations
#===============================================================================

from timeit import default_timer as timer


def main():
    loops = 10000

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(result)
    print(str((end - start)) + " seconds") 

def problem():
    multiples = set()
    counter = 1

    while True:
        m3 = 3 * counter
        m5 = 5 * counter

        if m3 >= 1000 and m5 >= 1000:
            break

        if m3 == m5:
            multiples.add(m3)
        
        else:
            multiples.add(m3)
        
            if m5 < 1000:
                multiples.add(m5)

        counter += 1
        
    return sum(multiples)

main()