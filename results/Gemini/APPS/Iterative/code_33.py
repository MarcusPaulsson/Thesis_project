def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def solve():
    a1, b1, a2, b2, L, R = map(int, input().split())

    g = gcd(a1, a2)

    if (b2 - b1) % g != 0:
        print(0)
        return

    lcm = (a1 * a2) // g

    # Find a solution to a1*x + a2*y = b2 - b1
    d, x, y = extended_gcd(a1, a2)
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g

    # Find a general solution:
    # x = x0 + (a2/g)*t
    # y = y0 - (a1/g)*t

    # We want to find the smallest x0 such that a1*x0 + b1 >= L and a2*y0 + b2 >= L
    # This is equivalent to finding the smallest t such that
    # a1*(x + (a2/g)*t) + b1 >= L and a2*(y - (a1/g)*t) + b2 >= L

    # Let's find the minimum value that satisfies a1*x + b1 = a2*y + b2
    first_val = a1 * x + b1

    # Adjust the value to be within the range [L, R]
    if first_val < L:
        k = (L - first_val + lcm - 1) // lcm
        first_val += k * lcm

    if first_val > R:
        print(0)
        return

    # Calculate the number of solutions
    count = (R - first_val) // lcm + 1

    print(count)

solve()