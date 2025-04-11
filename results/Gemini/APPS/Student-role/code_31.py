def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n <= 63 and k > (1 << n):
        print(1, 1)
        return

    num = 1
    den = 1
    twos_num = 0
    twos_den = 0

    for i in range(int(k)):
        if i == 0:
            continue
        val = pow(2, n, mod) - i
        num = (num * (val % mod)) % mod
        
        temp = i
        while temp % 2 == 0 and temp > 0:
            twos_num += 1
            temp //= 2
    
    den = pow(pow(2, n, mod), int(k - 1), mod) % mod
    
    temp = int(n * (k - 1))
    while temp % 2 == 0 and temp > 0:
        twos_den += 1
        temp //= 2

    if twos_num > twos_den:
        num = 0
    else:
        
        inv_den = pow(den, mod - 2, mod)
        num = (num * inv_den) % mod
    
    a = (1 - num + mod) % mod
    b = 1
    
    print(a, b)

solve()