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
    
    g, x, y = extended_gcd(a1, a2)
    
    if (b2 - b1) % g != 0:
        print(0)
        return
    
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g
    
    lcm = (a1 * a2) // g
    
    k = x
    
    k0 = k % (a2 // g)
    
    first_x = a1 * k0 + b1
    
    if first_x < L:
        diff = L - first_x
        num_lcm = (diff + lcm - 1) // lcm
        first_x += num_lcm * lcm
    
    if first_x > R:
        print(0)
        return
    
    count = (R - first_x) // lcm + 1
    
    
    
    
    
    
    k_min_a1 = (L - b1 + a1 - 1) // a1 if L > b1 else 0
    k_min_a2 = (L - b2 + a2 - 1) // a2 if L > b2 else 0
    
    
    
    
    
    
    
    valid_count = 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print(count)

solve()