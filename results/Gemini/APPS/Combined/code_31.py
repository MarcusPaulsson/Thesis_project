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

    power_of_2_n = pow(2, n, mod)
    
    if k > mod:
        print(1,1)
        return
    
    for i in range(k):
        if i == 0:
            continue
        val = (power_of_2_n - i) % mod
        num = (num * val) % mod
        
        v = i
        while v % 2 == 0 and v > 0:
            twos_num += 1
            v //= 2
            
    den = pow(power_of_2_n, k - 1, mod)
    
    v = den
    while v % 2 == 0 and v > 0:
        twos_den += 1
        v //= 2
    
    if twos_num > twos_den:
        num = 0
    else:
        twos_diff = twos_den - twos_num
        num = (num * pow(2, twos_diff, mod)) % mod
        
    a = (den - num + mod) % mod
    b = den % mod
    

    gcd_val = gcd(a, b)
    a //= gcd_val
    b //= gcd_val

    print(a % mod, b % mod)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

solve()