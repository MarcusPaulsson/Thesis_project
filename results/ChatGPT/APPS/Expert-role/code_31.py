def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_probability(n, k):
    MOD = 1000003
    days = 1 << n  # This is 2^n

    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the total outcomes B
    B = pow(days, k, MOD)

    # Calculate the favorable outcomes A
    favorable_outcomes = 1
    for i in range(k):
        favorable_outcomes *= (days - i)
        favorable_outcomes %= MOD

    # Probability of at least two people having the same birthday
    A = (B - favorable_outcomes) % MOD

    # Reduce A/B to irreducible form
    g = gcd(A, B)
    A //= g
    B //= g

    return A % MOD, B % MOD

n, k = map(int, input().split())
A, B = calculate_probability(n, k)
print(A, B)