#Problem 0005 - Smallest Multiple
#===============================================================================
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Answer: 232792560
#Time: 128.7871 Seconds Per 1,000,000 iterations
#===============================================================================
from functools import reduce
from timeit import default_timer as timer

def main():
    loops = 1

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(result)
    print(str((end - start)) + " seconds") 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b)//gcd(a, b)

def lcmm(multipule_list):
    return reduce(lambda x, y: lcm(x, y), multipule_list)

def problem():
    result = lcmm(list(range(20, 1, -1)))
    return result

main()