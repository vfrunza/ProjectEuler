#Problem 0003 - Largest Prime Factor
#===============================================================================
#The prime factors 13195 are 5, 7, 13,and 29.

#What is the largest prime factor of 600851475143

#Answer: 6857
#Time: 131.0388 Seconds Per 100 iterations
#===============================================================================

from math import sqrt
from Utility import prime_test

def problem():
    n = 600851475143

    for i in range(int(sqrt(n))-1, 2, -2):
        if prime_test(i):
            if n % i == 0:
                return i

