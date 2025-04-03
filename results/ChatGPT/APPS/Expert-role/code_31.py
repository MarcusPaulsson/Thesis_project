def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def probability_of_shared_birthday(n, k):
    MOD = 10**6 + 3
    days = 1 << n  # This is 2^n
    
    if k > days:
        return (1, 1)  # If k > days, probability is 1
    
    # Total ways to choose k birthdays
    total_ways = pow(days, k, MOD)
    
    # Calculate the ways to choose k birthdays with no shared birthday
    non_shared_ways = 1
    for i in range(k):
        non_shared_ways *= (days - i)
        non_shared_ways %= MOD
    
    # Probability of at least two having the same birthday
    shared_ways = (total_ways - non_shared_ways) % MOD
    
    # A and B
    A = shared_ways
    B = total_ways
    
    # Reduce A/B to its irreducible form
    divisor = gcd(A, B)
    A //= divisor
    B //= divisor
    
    return (A % MOD, B % MOD)

# Input reading
n, k = map(int, input().split())
result = probability_of_shared_birthday(n, k)
print(result[0], result[1])