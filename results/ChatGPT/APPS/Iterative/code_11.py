def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)
    
    # Calculate the maximum chocolates
    chocolates_a = count_a * p
    chocolates_b = count_b * q
    
    # If p > q, prioritize Red (a), otherwise prioritize Blue (b)
    if p > q:
        chocolates = chocolates_a + (count_b - count_ab) * q
    else:
        chocolates = chocolates_b + (count_a - count_ab) * p
    
    return chocolates

# Input
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))