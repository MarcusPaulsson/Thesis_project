def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inv(a, p):
    return pow(a, p - 2, p)

def birthday_paradox(n, k):
    MOD = 1000003
    days = 1 << n  # 2^n
    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no collision
    prob_no_collision = 1
    for i in range(k):
        prob_no_collision *= (days - i)
        prob_no_collision %= MOD

    # Total possible birthday assignments
    total_assignments = pow(days, k, MOD)

    # Probability of at least one collision
    A = (total_assignments - prob_no_collision) % MOD
    B = total_assignments

    # Reduce A and B by their gcd
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd

    return A % MOD, B % MOD

# Read input
n, k = map(int, input().split())
result = birthday_paradox(n, k)
print(result[0], result[1])