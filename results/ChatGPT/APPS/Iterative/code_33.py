def count_intersection(a1, b1, a2, b2, L, R):
    from math import gcd

    # Adjust b1 and b2 for the equations
    b1 = b1 % a1
    b2 = b2 % a2

    # Calculate the step size (lcm) and the gcd
    g = gcd(a1, a2)
    step = (a1 // g) * a2  # lcm(a1, a2)

    # Determine the values of x that satisfy both equations
    diff = (b2 - b1) % a2
    inv_a1 = pow(a1 // g, -1, a2 // g)  # Modular inverse
    t = (diff * inv_a1) % (a2 // g)

    # Particular solution x0
    x0 = b1 + a1 * t

    # Adjust x0 to be within the bounds [L, R]
    if x0 < L:
        x0 += ((L - x0 + step - 1) // step) * step
    elif x0 > R:
        return 0  # No valid solution if x0 is beyond R

    # Count the number of valid solutions in the range [L, R]
    last_valid = R - (R - x0) % step

    if last_valid < x0:
        return 0

    return (last_valid - x0) // step + 1

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
# Output the result
print(count_intersection(a1, b1, a2, b2, L, R))