def count_common_terms(a1, b1, a2, b2, L, R):
    from math import gcd

    # Normalize the sequences
    a1, b1 = a1, b1 % a1
    a2, b2 = a2, b2 % a2

    # Calculate the GCD of the differences
    g = gcd(a1, a2)

    # Check if the two sequences can produce common terms
    if (b2 - b1) % g != 0:
        return 0

    # Find the first term in the intersection of the two sequences
    x0 = (b2 - b1) // g * (a1 // g) % (a2 // g) * a1 + b1
    
    # Generate the first term in the sequence
    if x0 < L:
        x0 += ((L - x0 + a1 * a2 // g - 1) // (a1 * a2 // g)) * (a1 * a2 // g)
    elif x0 > R:
        return 0

    # Calculate the step size
    step = a1 * a2 // g

    # Calculate the last term within the range
    if x0 > R:
        return 0

    last = R // step * step + (b1 if last % step == b1 else 0)

    # Count the terms
    if x0 > last:
        return 0

    return (last - x0) // step + 1

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_common_terms(a1, b1, a2, b2, L, R)
print(result)