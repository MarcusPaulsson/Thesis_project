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

    lcm = (a1 * a2) // g

    x0 = x
    y0 = y
    
    
    def find_k_range(L, R, a1, b1, a2, b2, lcm, x0, y0):
      
        k_min = math.ceil((L - b1 - a1 * x0) / lcm)
        k_max = math.floor((R - b1 - a1 * x0) / lcm)
        
        return k_min, k_max
        
    k_min, k_max = find_k_range(L, R, a1, b1, a2, b2, lcm, x0, y0)

    count = 0
    
    for k in range(k_min, k_max + 1):
      val = a1 * (x0 + (lcm // a1) * k) + b1
      
      if L <= val <= R:
        
        k_prime = (val - b1) / a1
        l_prime = (val - b2) / a2
        
        if k_prime >= 0 and l_prime >= 0:
            count += 1

    print(count)

solve()