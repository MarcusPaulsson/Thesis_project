def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inv(a, m):
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
        return 1, 1  # Guaranteed a match

    prob_no_match = 1
    for i in range(k):
        prob_no_match *= (days - i) % MOD
        prob_no_match %= MOD
        prob_no_match *= mod_inv(days, MOD)
        prob_no_match %= MOD

    prob_match = (1 - prob_no_match + MOD) % MOD

    A = prob_match
    B = 1

    # Calculate A and B
    if prob_match > 0:
        A = (A * (days - k)) % MOD
        B = (B * days) % MOD
        prob_match -= 1

    # Reduce A and B
    common_divisor = gcd(A, B)
    A //= common_divisor
    B //= common_divisor

    return A % MOD, B % MOD

n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)