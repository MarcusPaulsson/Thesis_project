def count_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the least common multiple of the step sizes
    step = abs(a1 * a2 // gcd(a1, a2))
    
    # Determine the starting point based on the offsets
    start = max(b1, b2)
    offset = abs(b1 - b2)

    # Adjust start to the first valid x in the range
    if (start - offset) % step != 0:
        start += step - (start - offset) % step

    # Ensure start is at least L
    if start < L:
        start += ((L - start + step - 1) // step) * step

    # Count valid integers in the range [L, R]
    if start > R:
        return 0

    return (R - start) // step + 1

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_integers(a1, b1, a2, b2, L, R))