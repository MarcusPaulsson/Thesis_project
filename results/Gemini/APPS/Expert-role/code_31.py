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

    for i in range(k):
        if i == 0:
            continue
        val = pow(2, n, mod) - i
        num = (num * (val % mod)) % mod
        
        temp = i
        while temp % 2 == 0 and temp > 0:
            twos_num += 1
            temp //= 2
            
    den = pow(pow(2, n, mod), k - 1, mod)

    temp_den = k - 1
    while temp_den % 2 == 0 and temp_den > 0:
        twos_den += 1
        temp_den //= 2
    
    twos_den *= n
    
    
    twos_diff = twos_den - twos_num
    
    if twos_diff > 0:
        den = (den * pow(pow(2,twos_diff,mod),1,mod)) % mod
        
    
    
    
    
    
    
    
    
    inv_den = pow(den, mod - 2, mod)
    prob_diff = (num * inv_den) % mod
    
    
    
    
    a = (1 - prob_diff + mod) % mod
    b = 1
    
    
    
    
    
    print(a, 1)

solve()