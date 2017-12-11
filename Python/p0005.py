#Problem 0005 - Smallest Multiple
#===============================================================================
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Answer: 232792560
#===============================================================================
from functools import reduce
import Utility

def lcmm(multipule_list):
    return reduce(lambda x, y: Utility.lcm(x, y), multipule_list)

def problem():
    return lcmm([20,19,18,17,16,15,14,13,12,11]), "5"
