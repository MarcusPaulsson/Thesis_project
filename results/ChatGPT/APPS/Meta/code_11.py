def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red, Blue, and both
    red_tiles = n // a
    blue_tiles = n // b
    both_tiles = n // (a * b)
    
    # Total chocolates from Red tiles and Blue tiles
    total_chocolates = (red_tiles * p) + (blue_tiles * q) - (both_tiles * min(p, q))
    
    return total_chocolates

# Input
n, a, b, p, q = map(int, input().split())
# Output
print(max_chocolates(n, a, b, p, q))