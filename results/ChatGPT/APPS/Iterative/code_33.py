def count_common_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the step size and the least common multiple
    step = abs(a1 * a2 // gcd(a1, a2))

    # Function to find the first valid x in the range [L, R] for a given progression
    def first_valid_x(a, b):
        if a == 0:
            return b if L <= b <= R else None
        k = (L - b + a - 1) // a
        x = a * k + b
        return x if L <= x <= R else None

    # Function to find the last valid x in the range [L, R] for a given progression
    def last_valid_x(a, b):
        if a == 0:
            return b if L <= b <= R else None
        k = (R - b) // a
        x = a * k + b
        return x if L <= x <= R else None

    # Get the first and last valid x from both progressions
    x1 = first_valid_x(a1, b1)
    x2 = first_valid_x(a2, b2)

    if x1 is None or x2 is None:
        return 0

    # Calculate the first common x
    first_common = max(x1, x2)
    if (first_common - b1) % a1 != 0 or (first_common - b2) % a2 != 0:
        return 0

    # Calculate the last valid x
    last_common = min(last_valid_x(a1, b1), last_valid_x(a2, b2))
    if last_common is None or last_common < first_common:
        return 0

    # Count the number of valid integers in the range
    return (last_common - first_common) // step + 1

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Get the result
result = count_common_integers(a1, b1, a2, b2, L, R)
# Print the result
print(result)