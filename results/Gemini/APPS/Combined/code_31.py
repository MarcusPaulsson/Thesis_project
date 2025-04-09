def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 63 and k > 1:
        print(1, 1)
        return

    if k > 2**n:
        print(1, 1)
        return

    b = pow(2, n, mod)

    num = 1
    den = 1

    for i in range(int(k)):
        num = (num * (b - i)) % mod
        den = (den * b) % mod

    a = (den - num + mod) % mod

    from math import gcd
    g = gcd(a, den)
    print(a // g, den // g)

solve()