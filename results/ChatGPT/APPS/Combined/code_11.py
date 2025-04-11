def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red
    red_tiles = n // a
    # Calculate the number of tiles painted Blue
    blue_tiles = n // b
    # Calculate the number of tiles painted both Red and Blue (overlap)
    overlap_tiles = n // (a * b)
    
    # Total chocolates from Red tiles
    total_red_chocolates = red_tiles * p
    # Total chocolates from Blue tiles
    total_blue_chocolates = blue_tiles * q
    # Subtract the overlap since they are counted twice
    total_chocolates = total_red_chocolates + total_blue_chocolates - (overlap_tiles * min(p, q))
    
    return total_chocolates

# Example usage
if __name__ == "__main__":
    print(max_chocolates(5, 2, 3, 12, 15))  # Output: 39
    print(max_chocolates(20, 2, 3, 3, 5))   # Output: 51
    print(max_chocolates(1, 1, 1, 1, 1))     # Output: 1
    print(max_chocolates(1, 2, 2, 2, 2))     # Output: 0
    print(max_chocolates(2, 1, 3, 3, 3))     # Output: 6