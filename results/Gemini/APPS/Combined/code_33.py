def gcd(a, b):
    """Computes the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Computes the extended greatest common divisor of a and b,
    and finds coefficients x and y such that ax + by = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def solve():
    """Solves the problem of finding the number of integers x in the range [L, R] that
    satisfy x = a1*k + b1 = a2*l + b2 for some integers k and l.
    """
    a1, b1, a2, b2, L, R = map(int, input().split())

    g = gcd(a1, a2)

    if (b2 - b1) % g != 0:
        print(0)
        return

    d, x, y = extended_gcd(a1, a2)
    x *= (b2 - b1) // d

    lcm = (a1 * a2) // g
    
    # Ensure x is a valid solution
    x0 = (x * a1 + b1)

    # Find the smallest value >= L that satisfies the condition
    if lcm == 0:
        first_val = x0
    else:
        k = (L - x0 + lcm - 1) // lcm
        first_val = x0 + k * lcm
    
    if first_val > R:
        print(0)
        return

    count = (R - first_val) // lcm + 1
    print(count)

solve()