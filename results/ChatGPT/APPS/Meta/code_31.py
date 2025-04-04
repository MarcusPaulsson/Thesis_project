def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def birthday_paradox(n, k):
    MOD = 1000003
    days = 1 << n  # This is 2^n

    if k > days:
        return 1, 1  # P(at least two share a birthday) = 1 when k > days

    # Calculate P(no two share a birthday)
    prob_no_shared = 1
    for i in range(k):
        prob_no_shared *= (days - i)
        prob_no_shared //= days  # As we multiply we can divide the days

    prob_shared = 1 - prob_no_shared  # P(at least two share a birthday)
    
    # Prob shared = (1 - P(no shared)) = (Days * Days * ... * Days - (Days - 0) * (Days - 1) * ... * (Days - k + 1)) / Days^k
    A = (days**k - prob_no_shared * days**k) % MOD
    B = days**k % MOD

    # Reduce A/B to be coprime
    common_divisor = gcd(A, B)
    A //= common_divisor
    B //= common_divisor

    return A % MOD, B % MOD

# Read input
n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)