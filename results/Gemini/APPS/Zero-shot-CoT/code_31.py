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

    
    days = pow(2, n, mod)
    
    for i in range(k):
        if i == 0:
            continue
        num = (num * (days - i + mod)) % mod
        den = (den * pow(2, n, mod)) % mod

        temp_i = i
        while temp_i % 2 == 0 and temp_i > 0:
            twos_num += 1
            temp_i //= 2

        temp_days = pow(2, n, mod)
        while temp_days % 2 == 0 and temp_days > 0:
            twos_den += 1
            temp_days //= 2
        
    
    twos_total = 0
    for i in range(1, int(k)):
        temp_i = i
        while temp_i % 2 == 0 and temp_i > 0:
            twos_total += 1
            temp_i //= 2

    twos_in_den = n * (k - 1)

    num_twos = 0
    temp = k - 1
    while temp > 0:
        num_twos += temp // 2
        temp //= 2
    
    if twos_in_den > num_twos:
        
        if twos_in_den > 0:
             
            
            num = (num * pow(pow(2, twos_in_den - num_twos, mod), mod - 2, mod)) % mod
            den = (den * pow(pow(2, num_twos, mod), mod - 2, mod)) % mod
        #num = (num * pow(pow(2, twos_in_den - num_twos, mod), mod - 2, mod)) % mod
        #den = (den * pow(pow(2, num_twos, mod), mod-2, mod)) % mod

        ans_num = (days - k + 1 + mod) % mod
        ans_den = pow(days, k - 1, mod)

        
        ans_num = (ans_num * pow(num, mod - 2, mod)) % mod
        ans_den = (ans_den * pow(den, mod - 2, mod)) % mod
        
        
        print((1 - ans_num + mod) % mod, ans_den)

    else:
        print(1 - (num * pow(den, mod-2, mod)) % mod, 1)
       
solve()