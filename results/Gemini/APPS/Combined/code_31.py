def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    num = 1
    den = 1
    
    twos_in_num = 0
    twos_in_den = 0

    for i in range(k):
        if i == 0:
            continue
        
        val = pow(2, n, mod) - i
        if val < 0:
            val += mod
        
        num = (num * val) % mod
        
        temp = i
        while temp > 0 and temp % 2 == 0:
            twos_in_num += 1
            temp //= 2
            
    twos_in_den = min(n * (k - 1), twos_in_num)
    
    den = pow(pow(2, n, mod), k - 1, mod)
    
    num_div = pow(2, twos_in_num, mod)
    den_div = pow(2, twos_in_den, mod)
    
    num = (num * pow(num_div, mod - 2, mod)) % mod
    den = (den * pow(den_div, mod - 2, mod)) % mod

    a = (mod + 1 - (num * pow(den, mod - 2, mod)) % mod) % mod
    b = 1

    print(a, b)

solve()