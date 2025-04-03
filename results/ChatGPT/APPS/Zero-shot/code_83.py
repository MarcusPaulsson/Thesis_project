def count_common_terms(a1, b1, a2, b2, L, R):
    from math import gcd

    # Normalize the progressions
    a1, b1, a2, b2 = a1, b1, a2, b2
    
    # Calculate the difference and gcd
    g = gcd(a1, a2)
    
    # Adjust b1 and b2 to find the intersection
    b_diff = b2 - b1
    
    # Check if the difference is a multiple of gcd
    if b_diff % g != 0:
        return 0
    
    # Find the first valid x
    a = (b_diff // g) * (a2 // g)
    b = (b_diff // g) * (a1 // g)
    
    # Find the first x such that x = a1 * k' + b1
    x_start = (a1 * max(0, (-b // a1) + 1) + b1) if a1 > 0 else b1
    
    # Calculate the step size
    step = lcm(a1, a2)
    
    # Calculate bounds
    if x_start < L:
        # Adjust to the next valid x
        x_start += ((L - x_start + step - 1) // step) * step
    
    if x_start > R:
        return 0
    
    # Count the number of valid x values
    count = (R - x_start) // step + 1
    
    return count

# Input
a1, b1, a2, b2, L, R = map(int, input().split())

# Output
print(count_common_terms(a1, b1, a2, b2, L, R))