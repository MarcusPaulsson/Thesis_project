def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if k > 2**n:
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
        num = (num * val) % mod

        twos = 0
        temp = i
        while temp > 0 and temp % 2 == 0:
            twos += 1
            temp //= 2
        twos_in_num += twos

    den = pow(pow(2, n, mod), k - 1, mod)
    
    twos_in_den = n * (k - 1)

    if twos_in_num > twos_in_den:
        num = 0
    elif twos_in_num < twos_in_den:
        den = 0
    else:
        
        twos = 0
        temp = num
        while temp > 0 and temp % 2 == 0:
            twos += 1
            temp //= 2
        
        twos2 = 0
        temp = den
        while temp > 0 and temp % 2 == 0:
            twos2 += 1
            temp //= 2
            
        num = num * pow(2, mod - 2, mod) % mod
        den = den * pow(2, mod - 2, mod) % mod
        
    a = (den - num + mod) % mod
    b = den
    
    print(a, b)

solve()