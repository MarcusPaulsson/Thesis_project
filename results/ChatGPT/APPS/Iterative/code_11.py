import math

def max_chocolates(n, a, b, p, q):
    # Count the number of tiles painted Red
    red_count = n // a
    # Count the number of tiles painted Blue
    blue_count = n // b
    # Count the number of tiles painted Red and Blue
    both_count = n // (a * b // math.gcd(a, b))
    
    # Calculate maximum chocolates
    # If we paint the overlapping tiles as Red
    option1 = (red_count - both_count) * p + (blue_count - both_count) * q + both_count * p
    # If we paint the overlapping tiles as Blue
    option2 = (red_count - both_count) * p + (blue_count - both_count) * q + both_count * q
    
    return max(option1, option2)

n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))