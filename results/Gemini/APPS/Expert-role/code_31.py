def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n >= 63 and k > 1:
        print(1, 1)
        return

    if k > (1 << n):
        print(1, 1)
        return

    numerator = 1
    denominator = 1
    
    days = pow(2, n, mod)
    
    for i in range(int(k)):
        numerator = (numerator * (days - i)) % mod
        denominator = (denominator * days) % mod
    
    
    
    def mod_inverse(a, m):
        m0 = m
        y = 0
        x = 1

        if (m == 1):
            return 0

        while (a > 1):

            q = a // m

            t = m
            m = a % m
            a = t
            t = y

            y = x - q * y
            x = t

        if (x < 0):
            x = x + m0

        return x
    
    
    inverse_denominator = mod_inverse(denominator, mod)
    
    probability_no_match = (numerator * inverse_denominator) % mod
    
    probability_match = (1 - probability_no_match + mod) % mod
    
    
    
    gcd_val = gcd(probability_match, mod)
    a = probability_match // gcd_val
    b = mod // gcd_val

    print(a % mod, b % mod)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()