def count_common_terms(a1, b1, a2, b2, L, R):
    # Start with the first arithmetic progression
    # x = a1 * k' + b1
    # Start with the second arithmetic progression
    # x = a2 * l' + b2

    # We will solve for the integer solutions
    from math import gcd
    
    # Calculate the difference and the modulo offset
    diff = a2 - a1
    offset = b1 - b2
    
    # If the sequences are the same
    if diff == 0:
        if (b1 - b2) % a1 == 0:
            # Find the first and last valid x within [L, R]
            first = max(L, b1)
            last = min(R, b1 + (R - b1) // a1 * a1)
            if first <= last:
                return (last - first) // a1 + 1
            else:
                return 0
        else:
            return 0

    # If the sequences are different, we'll find their intersection
    # We need to solve a1 * k' + b1 = a2 * l' + b2
    # Rearranging gives us: a1 * k' - a2 * l' = b2 - b1

    # Expressed in the form:
    # a1 * k' - a2 * l' = offset
    # We need integer solutions for k' and l'

    # Find the greatest common divisor
    g = gcd(a1, a2)

    # Check if offset is divisible by g
    if offset % g != 0:
        return 0

    # Scale down the equation
    a1 //= g
    a2 //= g
    offset //= g

    # Now we need to find k' and l' such that:
    # a1 * k' - a2 * l' = offset
    # where k', l' >= 0

    # The general solution for the diophantine equation can be derived
    # We need to find particular solutions first
    # Using extended Euclidean algorithm to find one solution
    def extended_gcd(x, y):
        if y == 0:
            return x, 1, 0
        g, x1, y1 = extended_gcd(y, x % y)
        return g, y1, x1 - (x // y) * y1

    g, x0, y0 = extended_gcd(a1, a2)

    # Scaling the solution to our offset
    x0 *= offset
    y0 *= offset

    # Now we have one particular solution (x0, y0)
    # General solution:
    # k' = x0 + (a2 // g) * t
    # l' = y0 + (a1 // g) * t

    # We need to find bounds on t such that k' >= 0 and l' >= 0
    a2_g = a2 // g
    a1_g = a1 // g

    # Finding bounds for t
    t_min_k = (-x0 + a2_g - 1) // a2_g if x0 < 0 else 0
    t_min_l = (-y0 + a1_g - 1) // a1_g if y0 < 0 else 0

    t_min = max(t_min_k, t_min_l)
    
    # Finding the maximum t such that within bounds
    # Substitute k' into the original range [L, R]
    # a1 * (x0 + a2_g * t) + b1 <= R
    # a1 * x0 + b1 + a1 * a2_g * t <= R
    # a1 * a2_g * t <= R - (a1 * x0 + b1)
    # t <= (R - (a1 * x0 + b1)) // (a1 * a2_g)

    t_max = (R - (a1 * x0 + b1)) // (a1 * a2_g) if a1 * a2_g > 0 else float('inf')

    # t is bounded between t_min and t_max
    if t_min > t_max:
        return 0
    
    return t_max - t_min + 1

# Reading input
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_common_terms(a1, b1, a2, b2, L, R)
print(result)