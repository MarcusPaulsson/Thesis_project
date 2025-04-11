def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 63 and k > 1:
        print(1, 1)
        return

    if k > (1 << n):
        print(1, 1)
        return

    num = 1
    den = 1
    
    for i in range(int(k)):
        num = (num * ((1 << n) % mod - i % mod)) % mod
        den = (den * ((1) % mod)) % mod

    den = pow((1 << (n * k)) % mod, mod - 2, mod)
    
    prob_diff = (num * den) % mod
    
    a = (1 - prob_diff + mod) % mod
    b = 1
    
    print(a, 1)

solve()