def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

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
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no collision
    prob_no_collision_numer = 1
    prob_no_collision_denom = 1
    for i in range(k):
        prob_no_collision_numer *= (days - i)
        prob_no_collision_denom *= days
        prob_no_collision_numer %= MOD
        prob_no_collision_denom %= MOD

    # Probability of at least one collision
    A = (prob_no_collision_denom - prob_no_collision_numer) % MOD
    B = prob_no_collision_denom

    # Reduce A/B to irreducible form
    common_divisor = gcd(A, B)
    A //= common_divisor
    B //= common_divisor

    return A % MOD, B % MOD

# Input reading
n, k = map(int, input().split())
result = birthday_paradox(n, k)
print(result[0], result[1])