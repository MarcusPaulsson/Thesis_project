def count_common_integers(a1, b1, a2, b2, L, R):
    from math import gcd

    def count_in_range(a, b, L, R):
        if a == 0:
            if b < L or b > R:
                return 0
            return R - L + 1
        start = (L - b + a - 1) // a  # ceil((L - b) / a)
        end = (R - b) // a            # floor((R - b) / a)
        return max(0, end - start + 1)

    # Calculate the gcd of the differences
    g = gcd(a1, a2)
    
    # Check if the equations can have common solutions
    if (b2 - b1) % g != 0:
        return 0

    # Calculate the values for k and l
    a1_g = a1 // g
    a2_g = a2 // g
    b_diff = b2 - b1
    b_diff_g = b_diff // g

    # Use the extended Euclidean algorithm to find a solution for modular equation
    # a1 * x ≡ b_diff (mod a2)
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    _, x0, y0 = extended_gcd(a1_g, a2_g)

    # Scale the solution to the specific b_diff
    x0 *= b_diff_g
    y0 *= b_diff_g

    # General solution
    x0 = (x0 % (a2_g)) * (g) + b1
    step = (a2_g * g)

    # Count valid x in range [L, R]
    count1 = count_in_range(step, x0, L, R)
    count2 = count_in_range(step, x0 + step, L, R)

    return count1 + count2

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Calculate and print the result
print(count_common_integers(a1, b1, a2, b2, L, R))