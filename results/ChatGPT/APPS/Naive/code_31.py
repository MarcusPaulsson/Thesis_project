def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def birthday_paradox(n, k):
    MOD = 1000003
    days = 1 << n  # 2^n

    if k > days:
        return 1, 1  # If more people than days, probability is 1

    # Calculate probability of all k people having distinct birthdays
    numerator = days
    denominator = days ** k

    for i in range(k):
        numerator *= (days - i)
        numerator %= MOD

    # Probability that at least two people share a birthday
    A = (denominator - numerator) % MOD
    B = denominator % MOD

    # Reduce A and B by their GCD
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd

    return A % MOD, B % MOD

# Read input
n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)