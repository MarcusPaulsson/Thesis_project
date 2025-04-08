def count_common_terms(a1, b1, a2, b2, L, R):
    def first_term(a, b, start):
        if a == 0:
            return b if b >= start else None
        n = (start - b + a - 1) // a  # ceil((start - b) / a)
        return a * n + b if n >= 0 else None
    
    def last_term(a, b, end):
        if a == 0:
            return b if b <= end else None
        n = (end - b) // a  # floor((end - b) / a)
        return a * n + b if n >= 0 else None

    # Find the first and last common terms for both sequences
    first_x = first_term(a1, b1, L)
    last_x = last_term(a1, b1, R)

    if first_x is None or last_x is None or first_x > R or last_x < L:
        return 0

    count_a1 = (last_x - first_x) // a1 + 1

    first_y = first_term(a2, b2, L)
    last_y = last_term(a2, b2, R)

    if first_y is None or last_y is None or first_y > R or last_y < L:
        return 0

    count_a2 = (last_y - first_y) // a2 + 1

    return min(count_a1, count_a2)

# Input
a1, b1, a2, b2, L, R = map(int, input().split())
# Output
print(count_common_terms(a1, b1, a2, b2, L, R))