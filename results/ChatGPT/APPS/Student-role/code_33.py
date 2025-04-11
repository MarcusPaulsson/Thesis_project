def count_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    # Calculate the difference and the starting point
    d = a2 - a1
    b_diff = b1 - b2

    # If the difference is zero, we need to check if they are equal
    if d == 0:
        if b1 == b2:
            return max(0, (R - L) // a1 + 1)
        else:
            return 0

    # Calculate the GCD of a1 and a2
    g = gcd(a1, a2)

    # Check if the difference is divisible by the GCD
    if b_diff % g != 0:
        return 0

    # Find the range of valid k' and l'
    # We need to solve the equation a1 * k' + b1 = a2 * l' + b2
    # Rearranging gives us: a1 * k' - a2 * l' = b2 - b1
    # This is a linear Diophantine equation

    # We can find a particular solution using the extended Euclidean algorithm
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    g, x0, y0 = extended_gcd(a1, a2)
    x0 *= b_diff // g
    y0 *= b_diff // g

    # Now we have a particular solution (x0, y0)
    # General solution is:
    # x = x0 + (a2/g) * t
    # y = y0 + (a1/g) * t
    # for integer t

    # We need to find the range of t such that L ≤ a1 * (x0 + (a2/g) * t) + b1 ≤ R
    # This simplifies to:
    # (L - b1) ≤ a1 * (x0 + (a2/g) * t) ≤ (R - b1)

    # Calculate bounds for t
    t1 = (L - b1 - a1 * x0) // (a1 * (a2 // g))
    t2 = (R - b1 - a1 * x0) // (a1 * (a2 // g))

    # Adjust bounds to ensure they are integers
    if (L - b1 - a1 * x0) % (a1 * (a2 // g)) > 0:
        t1 += 1
    if (R - b1 - a1 * x0) % (a1 * (a2 // g)) < 0:
        t2 -= 1

    return max(0, t2 - t1 + 1)

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_integers(a1, b1, a2, b2, L, R))