def max_chocolates(n, a, b, p, q):
    lcm = (a * b) // gcd(a, b)
    red_tiles = n // a
    blue_tiles = n // b
    both_tiles = n // lcm
    return max(red_tiles * p, blue_tiles * q)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))