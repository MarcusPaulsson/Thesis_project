def max_chocolates(n, a, b, p, q):
    red_tiles = n // a
    blue_tiles = n // b
    common_tiles = n // (a * b // gcd(a, b))
    
    # Calculate total chocolates by painting common tiles red or blue
    # Option 1: Paint common tiles red
    chocolates_red = red_tiles * p + (blue_tiles - common_tiles) * q
    
    # Option 2: Paint common tiles blue
    chocolates_blue = (red_tiles - common_tiles) * p + blue_tiles * q
    
    return max(chocolates_red, chocolates_blue)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Input reading
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))