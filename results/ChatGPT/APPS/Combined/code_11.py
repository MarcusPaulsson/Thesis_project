def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red
    red_tiles = n // a
    # Calculate the number of tiles painted Blue
    blue_tiles = n // b
    # Calculate the number of tiles painted both Red and Blue
    both_tiles = n // (a * b)

    # Calculate total chocolates for both scenarios
    total_chocolates_red = (red_tiles - both_tiles) * p + (blue_tiles * q)
    total_chocolates_blue = (blue_tiles - both_tiles) * q + (red_tiles * p)
    
    # Return the maximum of both scenarios
    return max(total_chocolates_red, total_chocolates_blue)

# Example usage
if __name__ == "__main__":
    n, a, b, p, q = map(int, input().split())
    print(max_chocolates(n, a, b, p, q))