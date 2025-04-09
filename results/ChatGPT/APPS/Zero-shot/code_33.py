def count_integers(a1, b1, a2, b2, L, R):
    from math import gcd
    
    # Calculate the difference in progressions and their coefficients
    d1 = a1
    d2 = a2
    b_diff = b2 - b1
    
    # Calculate the GCD of the two progressions
    g = gcd(d1, d2)
    
    # Check if there exists a solution for the linear combination
    if b_diff % g != 0:
        return 0
    
    # Find the general solution using the extended Euclidean algorithm
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y
    
    _, x0, y0 = extended_gcd(d1, d2)
    
    # Scale the solution
    x0 *= b_diff // g
    y0 *= b_diff // g
    
    # Coefficients for the general solution
    d1 //= g
    d2 //= g
    
    # Now we can express the integer solutions as:
    # x = x0 + k * (d2)
    # y = y0 - k * (d1)
    
    # We need x to be in range [L, R]
    # L <= x0 + k * d2 <= R
    # => (L - x0) / d2 <= k <= (R - x0) / d2
    
    def calc_k_bounds(x0, d, bound):
        if d > 0:
            return (bound - x0) // d
        elif d < 0:
            return (bound - x0 + d - 1) // d
        return float('inf')  # d == 0 case, which won't happen here
    
    # Calculate k bounds
    k_start = (L - x0 + (d2 - 1)) // d2 if d2 > 0 else (L - x0) // d2
    k_end = (R - x0) // d2 if d2 > 0 else (R - x0 + (d2 + 1)) // d2
    
    # The total number of valid k's is:
    count = max(0, k_end - k_start + 1)
    
    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_integers(a1, b1, a2, b2, L, R)
print(result)