def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k > mod:
        print(0, 1)
        return

    b = pow(pow(2, n, mod), k - 1, mod)
    a = 1
    num = 1
    
    for i in range(k - 1):
        num = (num * (pow(2, n, mod) - 1 - i) % mod) % mod
    
    a = (b - num + mod) % mod
    
    gcd_val = gcd(a, b)
    
    print(a // gcd_val % mod, b // gcd_val % mod)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()