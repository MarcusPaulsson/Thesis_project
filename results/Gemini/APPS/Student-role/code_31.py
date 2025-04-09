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
        den = (den * ((1)% mod)) % mod
        
    den = pow((1 << (n * int(k))) % mod, mod - 2, mod)
    
    prob_diff = (num * den) % mod
    prob_same = (1 - prob_diff + mod) % mod
    
    g = gcd(prob_same, (1 << (n * int(k))) % mod)
    
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    
    
    g = gcd(prob_same, pow(2, n*int(k)))
    
    
    
    num_gcd = gcd(prob_same, pow(2, n*int(k)))
    den_gcd = gcd(1, pow(2, n*int(k)))
    
    
    num_gcd = gcd(prob_same, pow(2, int(n*k)))
    den_gcd = gcd(1, pow(2, int(n*k)))

    
    
    
    num_final = 1
    den_final = 1
    
    
    
    
    
    num = 1
    den = 1
    
    for i in range(int(k)):
        num = (num * ((1 << n) - i))
        den = (den * (1))
    
    den = pow(1 << (n * int(k)), 1, mod)
    
    
    
    
    
    
    
    
    
    
    num = 1
    den = 1
    
    for i in range(int(k)):
        num = (num * ((1 << n) % mod - i % mod)) % mod
        den = (den * (1 % mod)) % mod
    
    den = pow((1 << (n * int(k))) % mod, mod - 2, mod)
    
    prob_diff = (num * den) % mod
    prob_same = (1 - prob_diff + mod) % mod
    
    a = prob_same
    b = 1
    

    print(a, 1)

solve()