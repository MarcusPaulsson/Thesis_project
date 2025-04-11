def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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

def birthday_paradox(n, k):
    MOD = 1000003
    days = 1 << n  # 2^n
    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no collision
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (days - i)
        denominator *= days
        numerator %= MOD
        denominator %= MOD

    # Probability of at least one collision
    A = (denominator - numerator) % MOD
    B = denominator

    # Reduce A/B to irreducible form
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd

    return A % MOD, B % MOD

# Input reading
n, k = map(int, input().split())
result = birthday_paradox(n, k)
print(result[0], result[1])