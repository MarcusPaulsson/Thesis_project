def min_traps(m, x):
    # Since GCD(x, m) = 1, x has a multiplicative inverse modulo m
    # The number of distinct rooms visited is equal to m / gcd(x, m) 
    # which is simply m as gcd(x, m) = 1.
    return m - 1

m, x = map(int, input().split())
print(min_traps(m, x))