#Problem 0007 - 10001st Prime
#===============================================================================
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

#Answer: 104743
#===============================================================================
from Utility import prime_test

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
