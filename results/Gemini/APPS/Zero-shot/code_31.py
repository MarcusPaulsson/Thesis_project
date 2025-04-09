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
        num = (num * ((pow(2, n, mod) - i + mod) % mod)) % mod
        den = (den * pow(2, n, mod)) % mod

    
    
    a = (den - num + mod) % mod if num != den else 0
    
    
    gcd_val = gcd(a,den)
    
    print(a // gcd_val, den // gcd_val)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()