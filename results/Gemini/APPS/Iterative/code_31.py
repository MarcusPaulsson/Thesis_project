def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n < 63 and k > (1 << n):
        print(1, 1)
        return

    def power(a, b, m):
        res = 1
        a %= m
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % m
            a = (a * a) % m
            b //= 2
        return res

    def inverse(a, m):
        return power(a, m - 2, m)

    B = power(2, n % (mod - 1) * (k - 1) % (mod - 1), mod)
    
    A_num = 1
    for i in range(k):
        A_num = (A_num * ((power(2, n % (mod - 1), mod) - i + mod) % mod)) % mod

    A = (B - A_num + mod) % mod
    

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_val = gcd(A, B)
    
    A = (A * inverse(gcd_val, mod)) % mod
    B = (B * inverse(gcd_val, mod)) % mod
    

    print(A, B)

solve()