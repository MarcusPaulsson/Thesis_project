def count_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the offset
    step = abs(a1 * a2 // gcd(a1, a2))
    
    # Calculate the starting points for both sequences
    start1 = (L - b1 + a1 - 1) // a1 * a1 + b1
    start2 = (L - b2 + a2 - 1) // a2 * a2 + b2

    # Calculate the first common point that is >= L
    if start1 < L:
        start1 += a1
    if start2 < L:
        start2 += a2

    # Find the first common value
    if start1 == start2:
        first_common = start1
    else:
        first_common = max(start1, start2)
        while (first_common - b1) % a1 != 0 or (first_common - b2) % a2 != 0:
            first_common += step

    # Now we need to find the last common value within [L, R]
    if first_common > R:
        return 0

    last_common = first_common + ((R - first_common) // step) * step

    # Calculate the number of integers
    return (last_common - first_common) // step + 1

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Get the result
result = count_integers(a1, b1, a2, b2, L, R)
# Print the result
print(result)