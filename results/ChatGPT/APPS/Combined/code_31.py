def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def birthday_paradox(n, k):
    MOD = 1000003
    days = 1 << n  # 2^n days
    if k > days:
        return 1, 1  # Guaranteed collision

    # Calculate the probability of no shared birthdays
    no_shared_birthdays = 1
    for i in range(k):
        no_shared_birthdays *= (days - i)
        no_shared_birthdays //= (i + 1)

    # Total outcomes
    total_outcomes = pow(days, k, MOD)

    # Probability of at least one shared birthday
    A = (total_outcomes - no_shared_birthdays) % MOD
    B = total_outcomes

    # Reduce A and B to their irreducible forms
    g = gcd(A, B)
    A //= g
    B //= g
    
    # Ensure A and B are within bounds after reduction
    A %= MOD
    B %= MOD
    
    return A, B

# Input
n, k = map(int, input().split())
result = birthday_paradox(n, k)
print(result[0], result[1])