def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    num = 1
    den = 1
    twos_num = 0
    twos_den = 0

    for i in range(int(k)):
        if i == 0:
            continue
        val = (pow(2, n, mod) - i) % mod
        num = (num * val) % mod
        
        temp = i
        while temp > 0 and temp % 2 == 0:
            twos_num += 1
            temp //= 2

    den = pow(pow(2, n, mod), int(k - 1), mod)
    twos_den = (int(k - 1) * int(n))
    
    twos_diff = twos_den - twos_num
    
    if twos_diff > 0:
        num = (num * pow(2, min(twos_diff, 60), mod)) % mod
        den = (den * pow(pow(2, min(twos_diff, 60), mod), mod - 2, mod)) % mod
    
    a = (den - num) % mod
    b = den % mod
    
    gcd_val = gcd(a, b)
    
    a = (a // gcd_val) % mod
    b = (b // gcd_val) % mod
    
    print(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()