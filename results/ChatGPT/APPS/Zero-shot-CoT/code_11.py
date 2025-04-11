def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b // gcd(a, b))
    
    # Calculate chocolates
    chocolates = count_a * p + count_b * q - count_ab * min(p, q)
    
    return chocolates

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Input
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))