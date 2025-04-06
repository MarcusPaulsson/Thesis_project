from math import gcd

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
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g

    lcm = a1 * a2 // g

    x0 = (x * a1 + b1) 
    
    k = (L - x0 + lcm - 1) // lcm
    x0 += k * lcm
    
    if x0 > R:
        print(0)
        return

    print((R - x0) // lcm + 1)

solve()