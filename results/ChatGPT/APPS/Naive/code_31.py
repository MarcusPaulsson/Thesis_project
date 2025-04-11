def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def birthday_paradox(n, k):
    MOD = 1000003

    if k > (1 << n):
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no shared birthdays
    numerator = 1
    denominator = 1 << n  # 2^n

    for i in range(k):
        numerator *= (denominator - i)
        numerator %= MOD
        denominator *= (1 << n)
        denominator %= MOD

    # Probability of at least one shared birthday
    A = (denominator - numerator) % MOD
    B = denominator % MOD

    # Reduce A/B to irreducible form
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd

    return A % MOD, B % MOD

# Input reading
n, k = map(int, input().split())
result = birthday_paradox(n, k)
print(result[0], result[1])