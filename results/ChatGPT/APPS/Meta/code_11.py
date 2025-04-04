def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red, Blue and both
    red_tiles = n // a
    blue_tiles = n // b
    both_tiles = n // (a * b)

    # Calculate the maximum chocolates
    # Calculate chocolates if we paint all tiles Red then Blue
    total_chocolates_red_first = (red_tiles - both_tiles) * p + (blue_tiles * q)
    
    # Calculate chocolates if we paint all tiles Blue then Red
    total_chocolates_blue_first = (blue_tiles - both_tiles) * q + (red_tiles * p)

    # Take the maximum
    return max(total_chocolates_red_first, total_chocolates_blue_first)

# Example usage
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))