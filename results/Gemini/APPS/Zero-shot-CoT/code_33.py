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

    lcm = (a1 * a2) // g

    d, x, y = extended_gcd(a1, a2)
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g

    x0 = x
    y0 = y

    k = math.ceil(-x0 / (a2 // g))
    x0 += k * (a2 // g)
    y0 -= k * (a1 // g)

    first_val = a1 * x0 + b1
    
    if first_val < min(b1, b2):
        k = math.ceil((min(b1, b2) - first_val) / lcm)
        first_val += k * lcm

    
    if first_val < L:
        k = math.ceil((L - first_val) / lcm)
        first_val += k * lcm
    

    if first_val > R:
        print(0)
        return

    count = (R - first_val) // lcm + 1
    if count < 0:
        print(0)
        return
    
    
    
    k_min = 0
    if (first_val - b1) % a1 != 0:
        print(0)
        return
    k_min = (first_val - b1) // a1

    if k_min < 0:
        
        k_add = math.ceil(-k_min / (lcm // a1))
        first_val += k_add * lcm
        if first_val > R:
          print(0)
          return
        count = (R - first_val) // lcm + 1
        if count < 0:
          print(0)
          return
        

    k_min2 = 0
    if (first_val - b2) % a2 != 0:
        print(0)
        return
    k_min2 = (first_val - b2) // a2
    
    if k_min2 < 0:
        k_add = math.ceil(-k_min2 / (lcm // a2))
        first_val += k_add * lcm
        if first_val > R:
          print(0)
          return
        count = (R - first_val) // lcm + 1
        if count < 0:
          print(0)
          return
    
    print(count)

solve()