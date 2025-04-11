def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // lcm(a, b)
    
    # Calculate chocolates if we prioritize Red or Blue
    chocolates_if_red_first = (count_a - count_ab) * p + (count_b - count_ab) * q + count_ab * max(p, q)
    chocolates_if_blue_first = (count_b - count_ab) * q + (count_a - count_ab) * p + count_ab * max(p, q)
    
    return max(chocolates_if_red_first, chocolates_if_blue_first)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * (y // gcd(x, y))

# Read input
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))