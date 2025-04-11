def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b // gcd(a, b))
    
    # Calculate chocolates if we paint Red first
    chocolates_red_first = (count_a - count_ab) * p + (count_b - count_ab) * q + count_ab * max(p, q)
    
    # Calculate chocolates if we paint Blue first
    chocolates_blue_first = (count_b - count_ab) * q + (count_a - count_ab) * p + count_ab * max(p, q)
    
    return max(chocolates_red_first, chocolates_blue_first)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Example usage
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))