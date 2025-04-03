def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3
    
    if k > 2**n:
        print(1, 1)
        return
    
    num = 1
    den = 1
    
    for i in range(int(k)):
        num = (num * (pow(2, n, mod) - i)) % mod
        den = (den * pow(2, n, mod)) % mod
    
    gcd = 1
    
    inv_den = pow(den, mod - 2, mod)
    
    p_diff = (num * inv_den) % mod
    
    a = (1 - p_diff + mod) % mod
    b = 1
    
    print(a, 1)

solve()