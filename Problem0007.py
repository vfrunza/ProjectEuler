#Problem 0007 - 10001st Prime
#===============================================================================
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#Answer: 104743
#First Version Time: 15.6768 Seconds Per 100 iterations
#Second Version Time:
#===============================================================================
import math
from timeit import default_timer as timer

def main():
    loops = 10

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(result)
    print(str((end - start)) + " seconds") 

def prime_test(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def problem():
    prime = 2
    prime_counter = 0
    while True:
        if prime_test(prime):
            prime_counter += 1
        if prime_counter == 10001:
            break
        prime += 1
    return prime

main()