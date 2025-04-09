def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def modular_inverse(a, m):
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
    mod = 1000003
    days = 1 << n  # 2^n days
    if k > days:
        # If k > days, probability is 1
        return 1, 1
    
    # Calculate the probability of no shared birthdays
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (days - i)) % mod
        denominator = (denominator * days) % mod

    # P(at least one shared birthday) = 1 - P(no shared birthdays)
    P_no_shared = (numerator * modular_inverse(denominator, mod)) % mod
    P_shared = (1 - P_no_shared + mod) % mod

    # P_shared is in the form of A / B
    A = P_shared
    B = 1

    # Now we need to express A / B correctly
    # B is days^k
    B = pow(days, k, mod)

    # A is the numerator of the probability
    A = (B - P_no_shared + mod) % mod

    # Reduce A/B to irreducible form
    common_gcd = gcd(A, B)
    A //= common_gcd
    B //= common_gcd

    return A, B

# Read input
n, k = map(int, input().split())
A, B = birthday_paradox(n, k)
print(A, B)