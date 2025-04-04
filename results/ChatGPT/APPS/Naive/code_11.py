def max_chocolates(n, a, b, p, q):
    # Count how many tiles can be painted Red
    count_red = n // a
    # Count how many tiles can be painted Blue
    count_blue = n // b
    # Count how many tiles can be painted both Red and Blue
    count_both = n // (a * b // gcd(a, b))

    # Calculate total chocolates if we prioritize Red or Blue
    chocolates_red_priority = (count_red - count_both) * p + (count_blue * q)
    chocolates_blue_priority = (count_blue - count_both) * q + (count_red * p)

    # Return the maximum of both strategies
    return max(chocolates_red_priority, chocolates_blue_priority)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Read input values
n, a, b, p, q = map(int, input().split())
# Print the maximum number of chocolates
print(max_chocolates(n, a, b, p, q))