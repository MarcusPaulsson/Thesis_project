from math import gcd

def count_common_terms(a1, b1, a2, b2, L, R):
    # Normalize b1 and b2 to the same form
    b1_mod_a1 = b1 % a1
    b2_mod_a2 = b2 % a2

    # Find the step size using the gcd
    step = abs(a1 * a2 // gcd(a1, a2))

    # Find the first valid x in the range [L, R]
    first_x = None
    for k in range(max(0, (L - b1) // a1), (R - b1) // a1 + 1):
        x = a1 * k + b1
        if L <= x <= R:
            first_x = x
            break

    if first_x is None:
        return 0

    # Adjust first_x to satisfy the second equation
    if (first_x - b2) % a2 != 0:
        first_x += (a2 - (first_x - b2) % a2) % a2

    if first_x > R:
        return 0

    # Calculate the count of valid x's in the range [L, R]
    count = (R - first_x) // step + 1
    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_common_terms(a1, b1, a2, b2, L, R))