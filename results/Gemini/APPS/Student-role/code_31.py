def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 63 and k > 1:
        print(1, 1)
        return

    if k > 2**n:
        print(1, 1)
        return

    num = 1
    den = 1
    
    for i in range(int(k)):
        num = (num * (pow(2, n, mod) - i)) % mod
        den = (den * pow(2, n, mod)) % mod

    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def mod_inv(a, m):
        return pow(a, m - 2, m)

    
    prob_same = (1 - (num * mod_inv(den, mod)) % mod + mod) % mod
    
    print(prob_same, 1)
    
solve()