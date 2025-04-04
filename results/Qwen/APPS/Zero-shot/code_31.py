from math import gcd
from functools import reduce

MOD = 10**6 + 3

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def factorial_mod(n, mod):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def power_mod(x, y, mod):
    result = 1
    x = x % mod
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % mod
        y = y >> 1
        x = (x * x) % mod
    return result

def birthday_paradox(n, k):
    days = power_mod(2, n, MOD)
    if k > days:
        return 1, 1
    numerator = reduce(lambda x, y: x * y % MOD, (days - i for i in range(k)))
    denominator = power_mod(days, k, MOD)
    common_divisor = gcd(numerator, denominator)
    A = numerator // common_divisor
    B = denominator // common_divisor
    return A, B

n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)