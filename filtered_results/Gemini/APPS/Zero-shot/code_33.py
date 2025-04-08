import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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
    x *= (b2 - b1) // d
    y *= (b2 - b1) // d
    
    x0 = x
    y0 = y
    
    k = (x0 % (a2 // g) + (a2 // g)) % (a2 // g)
    
    x = x0 - k * (a2 // g)
    y = y0 + k * (a1 // g)

    first_val = a1 * x + b1
    
    
    if first_val < max(b1, b2):
        k_adjust = (max(b1,b2) - first_val + lcm - 1) // lcm
        first_val += k_adjust * lcm
    
    
    
    if first_val < 0 :
        k_adjust = (-first_val + lcm -1 ) // lcm
        first_val += k_adjust * lcm
    
    
    
    
    if first_val < max(b1,b2):
        k_adjust = (max(b1,b2) - first_val + lcm -1) // lcm
        first_val += k_adjust * lcm
    
    
    
    
    if first_val < L:
      k_adjust = (L - first_val + lcm - 1) // lcm
      first_val += k_adjust * lcm
      
    if first_val > R:
      print(0)
      return

    
    count = (R - first_val) // lcm + 1
    
    print(count)
    
solve()