def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)
    
    # Calculate chocolates if red tiles are prioritized
    chocolates_red_first = (count_a - count_ab) * p + (count_b - count_ab) * q
    
    # Calculate chocolates if blue tiles are prioritized
    chocolates_blue_first = (count_b - count_ab) * q + (count_a - count_ab) * p
    
    # Return the maximum chocolates from both strategies
    return max(chocolates_red_first, chocolates_blue_first)

# Read input
n, a, b, p, q = map(int, input().split())

# Calculate and print the result
print(max_chocolates(n, a, b, p, q))