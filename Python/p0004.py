#Problem 0004 - Largest Palindrome Product
#===============================================================================
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#Answer: 906609
#===============================================================================

def problem():
    largest = 0
    for x in range(999, 100, -1):
        for y in range(x, 100, -1):

            currentInt = x * y
            current = str(currentInt)
            #print(int(current), largest)
            if currentInt > largest:
                if len(current) == 5:
                    if current[0] == current[4] and current[1] == current[3]:
                        if currentInt > largest:
                            largest = currentInt
                else:
                    if current[0] == current[5] and current[1] == current[4] and current[2] == current[3]:
                        if currentInt > largest:
                            largest = currentInt

    return largest, "4"

