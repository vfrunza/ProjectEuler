#Utility Library for Project Euler
#===============================================================================
#Below is a list of a variety of functions and classes that are used by many 
#problems in project euler.
#===============================================================================

import math

def save(problem, time):
    result_file = open("results.csv", "r+")
    result = result_file.readlines()

    results = []
    updated = False

    for line in result:
        results.append(line.strip("\n").split(","))

    for line in results:
        if line[0] == problem:
            line[1] = time
            updated = True
            break

    if updated == False:
        results.append([problem, time])

    result_file.seek(0)
    result_file.truncate()

    for line in results:
        result_file.write(str(line[0]) + "," + str(line[1]) + "\n")
    
    result_file.close()

#returns a list of factors of n.
def factorize(n):
    factors = []
    for i in range(n, 0, -1):
        if n % i == 0:
            if i not in factors:
                factors.append(i)
    return factors

#returns a list of prime factors of n
def pr_factorize(n, factors):
    if factors == None:
        factors = []
    
    if n % 2 == 0:
        factors.append(2)
        return pr_factorize(n / 2, factors)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i:
            factors.append(i)
            break
            
    else:
        factors.append(int(n))
        return factors
    return pr_factorize(n / i, factors)

#tests if n is prime, returns true/false
def prime_test(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

#Description: Finds the GCD between any two numbers.
#Returns: int Greatest Common Denominator
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#===LCM==========================================================================
#Description: Returns the lowest common multipule between any two numbers.
#Result: int LCM
#================================================================================
def lcm(a, b):
    return (a * b)//gcd(a, b)
