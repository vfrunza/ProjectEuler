#Problem 0004 - Largest Palindrome Product
#===============================================================================
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#Answer: 906609
#Time: 176.2876 Seconds Per 1,000 iterations
#===============================================================================

from timeit import default_timer as timer

def main():
    loops = 1000

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(result)
    print(str((end - start)) + " seconds") 

def problem():
    largest = 0
    for x in range(999, 450, -1):
        for y in range(999, 100, -1):

            current = str(x * y)
            #print(int(current), largest)
            if int(current) > largest:
                if len(current) == 5:
                    if current[0] == current[4] and current[1] == current[3]:
                        if int(current) > largest:
                            largest = int(current)

                else:
                    if current[0] == current[5] and current[1] == current[4] and current[2] == current[3]:
                        if int(current) > largest:
                            largest = int(current)

    return largest

main()
