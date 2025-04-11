def gcd(a, b):
    """Calculates the greatest common divisor (GCD) of two integers."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """
    Calculates the extended GCD of two integers a and b.

    Returns:
        A tuple (d, x, y) where d is the GCD of a and b, and x and y are
        integers such that ax + by = d.
    """
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def solve():
    """
    Solves the problem of finding the number of integers x in the range [L, R]
    that can be expressed in the form a1*k + b1 and a2*l + b2, where k and l
    are non-negative integers.
    """
    a1, b1, a2, b2, L, R = map(int, input().split())

    g = gcd(a1, a2)

    if (b2 - b1) % g != 0:
        print(0)
        return

    d, x, y = extended_gcd(a1, a2)
    x *= (b2 - b1) // d
    y *= (b2 - b1) // d

    lcm = (a1 * a2) // g

    # x = a1 * k + b1 = a2 * l + b2
    # k = k0 + (a2 // g) * t
    # l = l0 + (a1 // g) * t
    # x = a1 * (k0 + (a2 // g) * t) + b1
    # x = a1 * k0 + b1 + (a1 * a2 // g) * t
    # x = a1 * k0 + b1 + lcm * t

    x0 = a1 * x + b1  # Initial value of x

    # Find the range of t such that L <= x0 + lcm * t <= R
    t_min = (L - x0 + lcm - 1) // lcm
    t_max = (R - x0) // lcm

    count = 0
    for t in range(t_min, t_max + 1):
        k = x + (a2 // g) * t
        l = y + (a1 // g) * t
        if k >= 0 and l >= 0:
            count += 1

    print(count)

solve()