def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def birthday_paradox(n, k):
    MOD = 10**6 + 3
    days = 1 << n  # 2^n
    
    if k > days:
        return 1, 1  # Guaranteed to have at least one shared birthday
    
    # Calculate the probability of no shared birthdays
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= (days - i)
        denominator *= days
        if numerator >= MOD:
            numerator %= MOD
        if denominator >= MOD:
            denominator %= MOD

    # Probability of at least one shared birthday
    prob_shared_num = (denominator - numerator + MOD) % MOD
    prob_shared_den = denominator % MOD
    
    # Reduce fraction
    common_gcd = gcd(prob_shared_num, prob_shared_den)
    prob_shared_num //= common_gcd
    prob_shared_den //= common_gcd
    
    # Apply modulo to ensure coprimality
    prob_shared_num %= MOD
    prob_shared_den %= MOD
    
    return prob_shared_num, prob_shared_den

# Read input
n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)