def max_chocolates(n, a, b, p, q):
    # Count the number of tiles that can be painted Red
    count_red = n // a
    # Count the number of tiles that can be painted Blue
    count_blue = n // b
    # Count the number of tiles that can be painted both Red and Blue
    count_both = n // (a * b // gcd(a, b))
    
    # Calculate the total chocolates for both scenarios
    total_chocolates_red_first = (count_red - count_both) * p + count_blue * q
    total_chocolates_blue_first = (count_blue - count_both) * q + count_red * p
    
    # Return the maximum chocolates obtainable
    return max(total_chocolates_red_first, total_chocolates_blue_first)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Read input
n, a, b, p, q = map(int, input().split())
# Calculate and print the maximum chocolates
print(max_chocolates(n, a, b, p, q))