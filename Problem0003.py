#Problem 0003 - Largest Prime Factor
#===============================================================================
#The prime factors 13195 are 5, 7, 13,and 29.

#What is the largest prime factor of 600851475143

#Answer: 6857
#Time: 131.0388 Seconds Per 100 iterations
#===============================================================================

import math
from timeit import default_timer as timer

def main():
    loops = 1

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(result)
    print(str((end - start)) + " seconds") 

def prime_test(n):
	if n <= 3:
		return n >= 2
	if n % 2 == 0 or n % 3 == 0:
		return False
	for i in range(5, int(math.sqrt(n)) + 1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	return True

def problem():
    n = 600851475143

    for i in range(int(math.sqrt(n))-1, 2, -2):
        if prime_test(i):
            if n % i == 0:
                return i

main()