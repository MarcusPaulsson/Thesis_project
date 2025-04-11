def count_common_terms(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the difference and the initial offset
    d1 = a1
    d2 = a2
    b_diff = b2 - b1

    # Calculate the gcd of the two differences
    g = gcd(d1, d2)

    # Check if the difference is divisible by gcd
    if b_diff % g != 0:
        return 0

    # Find the first solution to the equation a1 * k' + b1 = a2 * l' + b2
    # We can use the extended Euclidean algorithm to find one solution
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    _, x0, y0 = extended_gcd(d1, d2)
    x0 *= b_diff // g
    y0 *= b_diff // g

    # Now we have one solution (x0, y0)
    # General solution is:
    # x = x0 + (d2/g) * t
    # y = y0 - (d1/g) * t for integer t

    # We need to find the range of t such that L <= x <= R
    t_min = (L - (x0 + (d2 // g) * 0)) // (d2 // g)
    t_max = (R - (x0 + (d2 // g) * 0)) // (d2 // g)

    if (x0 + (d2 // g) * t_min) < L:
        t_min += 1
    if (x0 + (d2 // g) * t_max) > R:
        t_max -= 1

    return max(0, t_max - t_min + 1)

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Get the result
result = count_common_terms(a1, b1, a2, b2, L, R)
# Print the result
print(result)