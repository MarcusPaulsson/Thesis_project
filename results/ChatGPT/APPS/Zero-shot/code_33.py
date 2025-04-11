def count_common_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the offset
    step = abs(a1 * a2 // gcd(a1, a2))
    
    # Find the first valid x in the range [L, R]
    def first_valid_x():
        for k in range((L - b1 + a1 - 1) // a1, (R - b1) // a1 + 1):
            x1 = a1 * k + b1
            if L <= x1 <= R:
                return x1
        return None

    # Find the last valid x in the range [L, R]
    def last_valid_x():
        for k in range((R - b1) // a1, (L - b1 - 1) // a1, -1):
            x1 = a1 * k + b1
            if L <= x1 <= R:
                return x1
        return None

    # Find the first valid x that satisfies both progressions
    def find_common_x(start):
        for l in range((start - b2 + a2 - 1) // a2, (R - b2) // a2 + 1):
            x2 = a2 * l + b2
            if x2 >= start and x2 <= R:
                return x2
        return None

    # Get the first valid x from the first progression
    x1 = first_valid_x()
    if x1 is None:
        return 0

    # Get the first common x that satisfies both progressions
    common_x = find_common_x(x1)
    if common_x is None:
        return 0

    # Count how many valid x's are in the range [L, R]
    count = 0
    while common_x <= R:
        if common_x >= L:
            count += 1
        common_x += step

    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_integers(a1, b1, a2, b2, L, R))