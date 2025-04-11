def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red
    red_tiles = n // a
    # Calculate the number of tiles painted Blue
    blue_tiles = n // b
    # Calculate the number of tiles painted both Red and Blue (common multiples)
    common_tiles = n // (a * b // gcd(a, b))
    
    # Calculate the maximum chocolates
    # We can either paint common tiles Red or Blue, choose the maximum
    max_chocolates = (red_tiles - common_tiles) * p + (blue_tiles - common_tiles) * q + common_tiles * max(p, q)
    
    return max_chocolates

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Input reading
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))