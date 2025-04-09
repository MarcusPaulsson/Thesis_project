def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k > mod:
        print(0, 1)
        return

    num = 1
    den = 1
    
    for i in range(int(k)):
        if i == 0:
            continue
        num = (num * (pow(2, n, mod) - i)) % mod
        den = (den * pow(2, n, mod)) % mod
    
    gcd_val = gcd(num, den)
    num //= gcd_val
    den //= gcd_val

    ans_num = (den - num + mod) % mod
    ans_den = den

    print(ans_num % mod, ans_den % mod)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()