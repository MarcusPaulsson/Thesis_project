def count_common_terms(a1, b1, a2, b2, L, R):
    from math import gcd

    if a1 == a2:
        if b1 == b2:
            # Both sequences are the same
            start = max(L, b1)
            end = min(R, b1 + ((R - b1) // a1) * a1)
            return (end - start) // a1 + 1 if start <= end else 0
        else:
            # Different sequences with the same step
            return 0

    # Ensure a1 < a2 for simplicity
    if a1 > a2:
        a1, b1, a2, b2 = a2, b2, a1, b1

    # Calculate the difference and gcd
    D = a2 - a1
    G = gcd(a1, D)

    # Find the range for valid x
    result = 0

    # Check for the start point
    for k in range(0, (R - b1) // a1 + 1):
        x = a1 * k + b1
        if x > R:
            break
        if x >= L:
            # Check if (x - b2) is a multiple of a2
            if (x - b2) % a2 == 0:
                result += 1

    return result

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
print(count_common_terms(a1, b1, a2, b2, L, R))