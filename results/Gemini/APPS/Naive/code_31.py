def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k > mod:
        print(1, 1)
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
    
    
    g = gcd(a, pow(2, int(n * (k-1)), mod))
    
    a = a // g
    b = pow(2, int(n * (k-1)), mod) // g
    
    print(a % mod, b % mod)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()