def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red, Blue, and both
    red_tiles = n // a
    blue_tiles = n // b
    both_tiles = n // (a * b)

    # Calculate the maximum chocolates
    max_chocolates = (red_tiles - both_tiles) * p + (blue_tiles - both_tiles) * q + both_tiles * max(p, q)

    return max_chocolates