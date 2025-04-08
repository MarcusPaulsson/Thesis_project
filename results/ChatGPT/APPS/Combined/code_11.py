def max_chocolates(n, a, b, p, q):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    red_tiles = n // a
    blue_tiles = n // b
    both_tiles = n // (a * b // gcd(a, b))

    total_chocolates = (red_tiles * p) + (blue_tiles * q) - (both_tiles * min(p, q))
    
    return total_chocolates

# Reading input
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))