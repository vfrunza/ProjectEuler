#Problem 0006 - Sum Square Difference
#===============================================================================
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Answer: 25164150
#Time: 3.4822 Seconds Per 100,000 iterations
#===============================================================================

def sum_of_squares(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i ** 2
    return total

def square_of_sum(limit):
    return sum(list(range(1, limit + 1))) ** 2

def problem():
    limit = 100
    return square_of_sum(limit) - sum_of_squares(limit), '"6. Sum Square Difference"'

