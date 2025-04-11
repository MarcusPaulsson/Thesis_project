def solve():
    n, k = map(int, input().split())
    mod = 10**6 + 3

    if n > 63 and k > 1:
        print(1, 1)
        return

    if k > 2**n:
        print(1, 1)
        return

    num = 1
    den = 1
    twos_num = 0
    twos_den = 0

    for i in range(k):
        val = (pow(2, n, mod) - i) % mod
        num = (num * val) % mod
        twos_num += count_twos(pow(2, n, 2**60) - i)

    den = pow(pow(2, n, mod), k, mod)
    twos_den = n * k

    twos_diff = min(twos_num, twos_den)

    num = (num * pow(2, mod - 1 - twos_diff % (mod - 1), mod)) % mod
    den = (den * pow(2, mod - 1 - twos_diff % (mod - 1), mod)) % mod

    a = (den - num + mod) % mod
    b = den % mod

    print(a, b)

def count_twos(n):
    count = 0
    while n > 0 and n % 2 == 0:
        count += 1
        n //= 2
    return count

solve()