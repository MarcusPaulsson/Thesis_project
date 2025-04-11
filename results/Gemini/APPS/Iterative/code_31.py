def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 63 and k > 1:
        print(1, 1)
        return

    if k > (1 << n):
        print(1, 1)
        return

    b = pow(pow(2, n, mod), k, mod)
    a = 1
    for i in range(k):
        a = (a * ((pow(2, n, mod) - i + mod) % mod)) % mod

    gcd_val = gcd(a, b)
    a //= gcd_val
    b //= gcd_val

    a = (b - a + mod) % mod
    print(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()