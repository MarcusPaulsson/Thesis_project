def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def probability_of_shared_birthday(n, k):
    days = 2 ** n
    if k > days:
        return 1, 1  # Guaranteed at least one shared birthday

    # Calculate the probability of no shared birthdays
    num = 1
    denom = days ** k
    for i in range(k):
        num *= (days - i)
    
    # The probability of at least two having the same birthday
    A = denom - num
    B = denom

    # Reduce A and B by their gcd
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd
    
    # Take modulo
    mod = 10**6 + 3
    A %= mod
    B %= mod
    
    return A, B

# Read input
n, k = map(int, input().split())
A, B = probability_of_shared_birthday(n, k)
print(A, B)