def count_common_terms(a1, b1, a2, b2, L, R):
    # Normalize b1 and b2 to be in the range of L to R
    def normalize(b, a, L, R):
        if a == 0:
            return b if L <= b <= R else None
        # Find the smallest k such that a * k + b >= L
        k_start = (L - b + a - 1) // a if a > 0 else (L - b) // a
        # Find the largest k such that a * k + b <= R
        k_end = (R - b) // a if a > 0 else (R - b + a - 1) // a
        return (k_start, k_end)

    # Get the ranges for k' for both progressions
    k1_range = normalize(b1, a1, L, R)
    k2_range = normalize(b2, a2, L, R)

    if k1_range is None or k2_range is None:
        return 0

    k1_start, k1_end = k1_range
    k2_start, k2_end = k2_range

    # Find the common terms
    common_terms = set()
    
    # Generate terms for the first progression
    for k in range(k1_start, k1_end + 1):
        common_terms.add(a1 * k + b1)

    # Count how many of these terms are also in the second progression
    count = 0
    for l in range(k2_start, k2_end + 1):
        term = a2 * l + b2
        if term in common_terms and L <= term <= R:
            count += 1

    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_terms(a1, b1, a2, b2, L, R))