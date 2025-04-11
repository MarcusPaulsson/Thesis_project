def count_common_ap(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the offset
    step = abs(a1 * a2 // gcd(a1, a2))
    
    # Calculate the first common term
    if a1 == a2:
        if b1 == b2:
            # If both sequences are identical
            start = max(L, b1)
            end = min(R, b1 + (R - b1) // a1 * a1)
            return (end - start) // a1 + 1 if start <= end else 0
        else:
            return 0
    
    # Find the first common term
    offset = (b2 - b1) % gcd(a1, a2)
    if offset != 0:
        return 0
    
    # Find the first term in the range [L, R]
    first_term = (b1 + a1 * ((L - b1 + a1 - 1) // a1)) if (L - b1) % a1 != 0 else L
    if first_term < L:
        first_term += step
    
    # Find the last term in the range [L, R]
    last_term = (b1 + a1 * ((R - b1) // a1))
    if last_term > R:
        last_term -= step
    
    # Count the number of terms
    if first_term > last_term:
        return 0
    
    return (last_term - first_term) // step + 1

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_ap(a1, b1, a2, b2, L, R))