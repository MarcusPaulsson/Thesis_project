import math

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

    d, x, y = extended_gcd(a1, a2)
    x *= (b2 - b1) // d
    y *= (b2 - b1) // d

    lcm = a1 * a2 // g

    x0 = x
    y0 = y

    t = math.ceil((-x0) / (a2 // g))
    x0 += (a2 // g) * t
    y0 -= (a1 // g) * t

    val = a1 * x0 + b1
    
    if val < L:
        t = math.ceil((L - val) / lcm)
        val += lcm * t
    
    if val > R:
        print(0)
        return

    count = (R - val) // lcm + 1
    print(count)

solve()