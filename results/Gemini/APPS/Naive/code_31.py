def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 63 and k > 1:
        print(1, 1)
        return

    if k > 2**n:
        print(1, 1)
        return

    numerator = 1
    denominator = 1
    
    for i in range(int(k)):
        numerator = (numerator * (pow(2, n, mod) - i)) % mod
        denominator = (denominator * pow(2, n, mod)) % mod

    gcd_val = gcd(numerator, denominator)
    numerator //= gcd_val
    denominator //= gcd_val

    a = (denominator - numerator) % mod
    b = denominator % mod

    print(a, b)
    
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()