def max_chocolates(n, a, b, p, q):
    count_red = n // a
    count_blue = n // b
    count_both = n // (a * b // gcd(a, b))
    
    # Calculate chocolates
    chocolates = (count_red - count_both) * p + (count_blue - count_both) * q + count_both * max(p, q)
    
    return chocolates

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Input
n, a, b, p, q = map(int, input().split())
# Output
print(max_chocolates(n, a, b, p, q))