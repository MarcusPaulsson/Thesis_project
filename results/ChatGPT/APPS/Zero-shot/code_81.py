def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def birthday_paradox(n, k):
    days = 2 ** n
    
    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no collisions
    prob_no_collision_numerator = days
    prob_no_collision_denominator = days

    for i in range(1, k):
        prob_no_collision_numerator *= (days - i)
        prob_no_collision_denominator *= days

    # Probability of at least one collision
    A = prob_no_collision_denominator - prob_no_collision_numerator
    B = prob_no_collision_denominator

    # Simplify A/B
    common_divisor = gcd(A, B)
    A //= common_divisor
    B //= common_divisor

    # Modulo
    MOD = 10**6 + 3
    A %= MOD
    B %= MOD

    # Ensure A and B are coprime before modulo
    assert gcd(A, B) == 1

    return A, B

# Input reading
n, k = map(int, input().strip().split())
A, B = birthday_paradox(n, k)
print(A, B)