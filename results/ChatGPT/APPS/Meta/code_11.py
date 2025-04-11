def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red and Blue
    red_tiles = n // a
    blue_tiles = n // b
    both_tiles = n // (a * b)  # Tiles that can be painted both Red and Blue

    # Calculate the maximum chocolates
    # We can choose to paint the common tiles either Red or Blue
    # We will choose the option that gives us more chocolates
    max_chocolates = (red_tiles * p) + (blue_tiles * q) - (both_tiles * min(p, q))
    
    return max_chocolates

# Example usage
# n, a, b, p, q = map(int, input().split())
# print(max_chocolates(n, a, b, p, q))