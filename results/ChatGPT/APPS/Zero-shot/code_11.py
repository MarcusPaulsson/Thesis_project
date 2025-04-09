def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b // gcd(a, b))  # Using LCM to find common multiples

    # Calculate the maximum chocolates by choosing the best option for overlap
    red_chocolates = (count_a - count_ab) * p + count_ab * max(p, q)
    blue_chocolates = (count_b - count_ab) * q + count_ab * max(p, q)
    
    return max(red_chocolates, blue_chocolates)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Input reading
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))