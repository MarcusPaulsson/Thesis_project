def max_chocolates(n, a, b, p, q):
    red_tiles = n // a
    blue_tiles = n // b
    common_tiles = n // (a * b)  # Tiles that are both red and blue

    # Calculate the number of tiles that can only be painted red or blue
    only_red = red_tiles - common_tiles
    only_blue = blue_tiles - common_tiles

    # Calculate total chocolates
    total_chocolates = (only_red * p) + (only_blue * q) + (common_tiles * max(p, q))
    
    return total_chocolates

# Input reading
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))