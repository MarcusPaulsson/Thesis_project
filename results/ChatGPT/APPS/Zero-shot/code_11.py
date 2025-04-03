def max_chocolates(n, a, b, p, q):
    # Count tiles that can be painted Red
    count_red = n // a
    # Count tiles that can be painted Blue
    count_blue = n // b
    # Count tiles that can be painted both Red and Blue
    count_both = n // (a * b // gcd(a, b))
    
    # Calculate chocolates
    total_chocolates = (count_red * p) + (count_blue * q) - (count_both * min(p, q))
    
    return total_chocolates

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Read input
n, a, b, p, q = map(int, input().split())
# Print the result
print(max_chocolates(n, a, b, p, q))