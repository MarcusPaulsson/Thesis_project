def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def prob_birthday_paradox(n, k):
    days = 1 << n  # 2^n
    
    if k > days:
        return 1, 1  # Guaranteed at least one shared birthday
    
    # Calculate the probability of no shared birthdays
    num = 1
    den = days ** k
    
    for i in range(k):
        num *= (days - i)
    
    # Probability of at least one shared birthday
    prob_not_shared = num / den
    prob_shared = 1 - prob_not_shared
    
    # Convert to fraction A/B
    A = den - num
    B = den
    
    # Reduce A/B by their gcd
    g = gcd(A, B)
    A //= g
    B //= g
    
    # Take modulo
    mod = 10**6 + 3
    A %= mod
    B %= mod
    
    return A, B

# Read input
n, k = map(int, input().split())
A, B = prob_birthday_paradox(n, k)
print(A, B)