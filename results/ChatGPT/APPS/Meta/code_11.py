def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red
    red_tiles = n // a
    # Calculate the number of tiles painted Blue
    blue_tiles = n // b
    # Calculate the number of tiles painted both Red and Blue (common multiples)
    common_tiles = n // (a * b // gcd(a, b))
    
    # Total chocolates from Red tiles
    total_red_chocolates = red_tiles * p
    # Total chocolates from Blue tiles
    total_blue_chocolates = blue_tiles * q
    
    # Since common tiles can be painted either Red or Blue, we take the maximum of both scenarios
    # 1. Paint common tiles Red
    # 2. Paint common tiles Blue
    max_chocolates = max(total_red_chocolates + (blue_tiles - common_tiles) * q,
                         total_blue_chocolates + (red_tiles - common_tiles) * p)
    
    return max_chocolates

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Example usage
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))