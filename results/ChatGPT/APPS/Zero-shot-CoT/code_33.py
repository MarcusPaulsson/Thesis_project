def count_common_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the offset
    step = abs(a1 * a2 // gcd(a1, a2))
    
    # Find the first valid x in the range [L, R]
    def first_valid_x():
        for k in range((L - b1) // a1, (R - b1) // a1 + 2):
            x = a1 * k + b1
            if L <= x <= R:
                return x
        return None

    # Find the first valid x for the second progression
    def first_valid_y():
        for l in range((L - b2) // a2, (R - b2) // a2 + 2):
            y = a2 * l + b2
            if L <= y <= R:
                return y
        return None

    x_start = first_valid_x()
    y_start = first_valid_y()

    if x_start is None or y_start is None:
        return 0

    # Find the first common x
    if x_start < y_start:
        x_start = ((y_start - b1 + a1 - 1) // a1) * a1 + b1
    else:
        y_start = ((x_start - b2 + a2 - 1) // a2) * a2 + b2

    # Count the number of valid integers in the range
    count = 0
    for x in range(x_start, R + 1, step):
        if L <= x <= R:
            count += 1

    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_integers(a1, b1, a2, b2, L, R))