def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k == 2:
        pow_2_n_mod = pow(2, n, mod)
        print(1, pow_2_n_mod)
        return

    num = 1
    den = 1
    
    for i in range(int(k)):
        if i == 0:
            continue
        num = (num * (pow(2, n, mod) - i)) % mod
        den = (den * pow(2, n, mod)) % mod

    
    
    inv_den = pow(den, mod - 2, mod)
    prob_diff = (num * inv_den) % mod
    
    a = (1 - prob_diff + mod) % mod
    b = 1
    
    print(a, 1)

solve()