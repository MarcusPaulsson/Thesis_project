def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k > mod:
        print(0, 1)
        return

    numerator = 1
    denominator = 1
    
    for i in range(int(k)):
        numerator = (numerator * (pow(2, n, mod) - i)) % mod
        denominator = (denominator * pow(2, n, mod)) % mod

    gcd_val = gcd(numerator, denominator)
    numerator //= gcd_val
    denominator //= gcd_val

    ans_numerator = (denominator - numerator + mod) % mod
    ans_denominator = denominator

    gcd_val = gcd(ans_numerator, ans_denominator)
    ans_numerator //= gcd_val
    ans_denominator //= gcd_val
    
    print(ans_numerator, ans_denominator)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()