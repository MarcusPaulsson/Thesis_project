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
        
    gcd_val = gcd(num, den)
    num //= gcd_val
    den //= gcd_val
    
    ans_num = (den - num + mod) % mod
    ans_den = den
    
    print(ans_num, ans_den)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()