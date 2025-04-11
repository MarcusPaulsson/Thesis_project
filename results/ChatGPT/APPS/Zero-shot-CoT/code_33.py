def count_common_ap(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the offset
    step = abs(a1 * a2 // gcd(a1, a2))
    offset = b2 - b1

    # Find the first valid x in the range [L, R]
    def first_valid_x():
        if offset % gcd(a1, a2) != 0:
            return None  # No solution
        # Solve for k' in a1 * k' + b1 = x
        # x = a1 * k' + b1 => k' = (x - b1) / a1
        # We need to find the smallest x >= L
        start = (L - b1 + a1 - 1) // a1  # ceil((L - b1) / a1)
        start_x = a1 * start + b1
        if start_x < L:
            start_x += a1
        return start_x

    # Find the last valid x in the range [L, R]
    def last_valid_x():
        # We need to find the largest x <= R
        end = (R - b1) // a1  # floor((R - b1) / a1)
        end_x = a1 * end + b1
        if end_x > R:
            end_x -= a1
        return end_x

    first_x = first_valid_x()
    last_x = last_valid_x()

    if first_x is None or first_x > R or last_x < L:
        return 0

    # Count the number of valid x's in the range [first_x, last_x]
    count = (last_x - first_x) // step + 1
    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_ap(a1, b1, a2, b2, L, R))