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
        
        val = pow(2,n,mod) - i
        
        num = (num * (val % mod)) % mod

        twos = 0
        temp = i
        while temp > 0 and temp % 2 == 0:
            twos += 1
            temp //= 2
        twos_num += twos
        

    den = pow(pow(2,n,mod),k-1,mod)
    

    twos_den = 0
    temp = den
    count = 0

    twos_den = (n * (k-1))
    
    if twos_num > twos_den:
        num = 0
        den = 1
    elif twos_num == twos_den:
        pass
    else:
        twos_diff = twos_den - twos_num
        num = num
        den = den * pow(pow(2, twos_num, mod),mod - 2, mod) % mod
        num = num * pow(pow(2, twos_num, mod),mod - 2, mod) % mod
    
        
    a = (den - num) % mod
    b = den % mod

    print(a, b)

solve()