def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def mod_inv(a, p):
    return pow(a, p - 2, p)

def birthday_paradox(n, k):
    MOD = 1000003
    days = 1 << n  # 2^n
    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no collisions
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (days - i)
        denominator *= days
        numerator %= MOD
        denominator %= MOD

    # Probability of at least one collision
    A = (denominator - numerator) % MOD
    B = denominator % MOD

    # Reduce A/B to irreducible form
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd

    return A % MOD, B % MOD

# Read input
n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)