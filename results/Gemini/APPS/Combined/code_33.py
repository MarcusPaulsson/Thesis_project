import math

def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Extended Euclidean algorithm to find the greatest common divisor (GCD) of a and b,
    as well as the coefficients x and y such that ax + by = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def solve():
    a1, b1, a2, b2, L, R = map(int, input().split())

    # We want to find the number of integers x such that L <= x <= R and
    # x = a1*k + b1 = a2*l + b2 for some non-negative integers k and l.
    # This is equivalent to finding the number of solutions to the equation
    # a1*k + b1 = a2*l + b2, or a1*k - a2*l = b2 - b1, with the constraint
    # that L <= a1*k + b1 <= R and k, l >= 0.

    # First, we rewrite the equation as a1*k + a2*(-l) = b2 - b1.
    # We use the extended Euclidean algorithm to find a particular solution (x, y)
    # to the equation a1*x + a2*y = gcd(a1, a2).  Then, if (b2 - b1) is not a
    # multiple of gcd(a1, a2), there are no solutions.  Otherwise, we can scale
    # the particular solution to obtain a solution to the equation
    # a1*k - a2*l = b2 - b1.

    g = gcd(a1, a2)
    
    if (b2 - b1) % g != 0:
        print(0)
        return
    
    x, y, _ = extended_gcd(a1, a2)
    
    x *= (b2 - b1) // g
    y *= -(b2 - b1) // g

    # Now we have a particular solution (x, y) to the equation a1*k - a2*l = b2 - b1,
    # or a1*x - a2*y = b2 - b1.  The general solution is given by
    # k = x + (a2/g)*t, l = y + (a1/g)*t, for some integer t.  We want to find the
    # number of values of t such that k >= 0, l >= 0, and L <= a1*k + b1 <= R.

    # We have k = x + (a2/g)*t >= 0, so t >= -x*g/a2.
    # We have l = y + (a1/g)*t >= 0, so t >= -y*g/a1.
    # Let t_min = max(ceil(-x*g/a2), ceil(-y*g/a1)).

    a1_div_g = a1 // g
    a2_div_g = a2 // g

    t_min = max(math.ceil(-x / a2_div_g), math.ceil(-y / a1_div_g))

    # Now we have k = x + (a2/g)*t_min, l = y + (a1/g)*t_min, and we have k >= 0 and l >= 0.
    # We want to find the number of values of t >= t_min such that
    # L <= a1*(x + (a2/g)*t) + b1 <= R.
    # L <= a1*x + a1*(a2/g)*t + b1 <= R
    # L - a1*x - b1 <= a1*(a2/g)*t <= R - a1*x - b1
    # (L - a1*x - b1)*g/(a1*a2) <= t <= (R - a1*x - b1)*g/(a1*a2)

    first_val = a1 * (x + a2_div_g * t_min) + b1
    
    lcm = (a1 * a2) // g

    if first_val > R:
        print(0)
        return
    
    if first_val < L:
        diff = L - first_val
        num_lcm = math.ceil(diff / lcm)
        first_val += num_lcm * lcm

    if first_val > R:
        print(0)
        return
    
    count = (R - first_val) // lcm + 1
    print(count)
solve()