def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    if k > mod:
        print(0, 1)
        return

    num = 1
    den = 1
    twos = 0

    for i in range(k):
        if i == 0:
            continue
        val = (pow(2, n, mod) - i) % mod
        num = (num * val) % mod
        
        temp = i
        while temp % 2 == 0 and temp > 0:
            twos += 1
            temp //= 2

    den = pow(pow(2, n, mod), k - 1, mod) % mod
    

    two_pow = min(n * (k - 1), twos)

    
    num = (num * pow(pow(2, two_pow, mod), mod - 2, mod)) % mod
    den = (den * pow(pow(2, two_pow, mod), mod - 2, mod)) % mod
    
    a = (den - num) % mod
    b = den % mod

    print(a, b)

solve()