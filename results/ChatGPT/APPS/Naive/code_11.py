def max_chocolates(n, a, b, p, q):
    # Calculate the number of tiles painted Red and Blue
    count_red = n // a
    count_blue = n // b
    count_both = n // (a * b)

    # The actual number of Red and Blue tiles
    count_red_only = count_red - count_both
    count_blue_only = count_blue - count_both

    # Calculate total chocolates
    total_chocolates = (count_red_only * p) + (count_blue_only * q) + (count_both * max(p, q))

    return total_chocolates

# Read input
n, a, b, p, q = map(int, input().split())

# Get the result
result = max_chocolates(n, a, b, p, q)

# Print the result
print(result)