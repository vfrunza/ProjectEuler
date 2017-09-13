#Problem 0009 - Special Pythagorean Triplet
#===============================================================================
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2

#For eaample, 32 + 42 = 9 + 16 = 25 = 52.

#There eaists eaactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Answer: 31875000
#First Version Time: 23.6835 Seconds Per 1 iterations
#Second Version Time: 9.5334 Seconds Per 1 iterations
#Third Version Time: 0.4985 Seconds Per 1 iterations
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
    for a in range(1, 1000):
        b = a + 1
        c = b + 1
        while c <= 1000:
            while c**2 < a**2 + b**2:
                c += 1
            if a**2 + b**2 - c**2 == 0 and a + b + c == 1000:
                return a*b*c
            b += 1

main()