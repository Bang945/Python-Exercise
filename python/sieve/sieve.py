def sieve(limit):
    total = list(range(2, limit + 1))

    for base in range(2, limit):
        total = list(filter(lambda d: d == base or d % base != 0, total))
        
    return total