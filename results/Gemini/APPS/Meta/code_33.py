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
    
    x0 = (x0 % (a2 // g) + (a2 // g)) % (a2 // g)
        
    val = a1 * x0 + b1
    
    
    k_min = (L - val + lcm - 1) // lcm
    k_max = (R - val) // lcm
    
    if k_min > k_max:
        print(0)
        return
    
    first = val + k_min * lcm
    last = val + k_max * lcm
    
    if first > R or last < L:
        print(0)
        return
    
    count = k_max - k_min + 1
    
    print(count)

solve()