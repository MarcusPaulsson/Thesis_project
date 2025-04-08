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
    MOD = 10**6 + 3
    days = 1 << n  # Efficiently calculate 2^n

    if k > days:
        return 1, 1  # Guaranteed shared birthday

    prob_no_shared = 1
    for i in range(k):
        prob_no_shared = prob_no_shared * (days - i) % MOD

    total_prob = pow(days, k, MOD)
    prob_shared = (total_prob - prob_no_shared) % MOD

    common_divisor = gcd(prob_shared, total_prob)
    A = (prob_shared // common_divisor) % MOD
    B = (total_prob // common_divisor) % MOD

    return A, B

if __name__ == "__main__":
    n, k = map(int, input().split())
    result = birthday_paradox(n, k)
    print(result[0], result[1])