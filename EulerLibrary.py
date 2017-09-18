def factorize(n):
    factors = []
    for i in range(n, 0, -1):
        if n % i == 0:
            if i not in factors:
                factors.append(i)
    return factors

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

def prime_test(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True