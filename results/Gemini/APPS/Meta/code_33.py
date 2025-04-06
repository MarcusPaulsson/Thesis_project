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
    l = -y

    x0 = a1 * k + b1
    
    
    def find_min_val(a1, b1, a2, b2, L, R):
        first_val = max(b1, b2)
        
        if first_val > R:
            return -1
        
        
        g, x, y = extended_gcd(a1, a2)

        if (b2 - b1) % g != 0:
            return -1
        
        x *= (b2 - b1) // g
        y *= (b2 - b1) // g
        
        lcm = (a1 * a2) // g
        
        x0 = a1 * x + b1
        
        if(x0 < max(b1,b2)):
            diff = max(b1, b2) - x0
            k = (diff + a1 -1)//a1
            x0 += k * a1
        
        if(x0 < max(b1,b2)):
             diff = max(b1, b2) - x0
             k = (diff + a2 -1)//a2
             x0 += k * a2
        
        
        if x0 < L:
            diff = L - x0
            k = (diff + lcm - 1) // lcm
            x0 += k * lcm

        if x0 > R:
            return -1
        
        return x0
        
    first_val = find_min_val(a1, a1, a2, a2, L, R)
    
    
    if first_val == -1:
        print(0)
        return
    
    
    g, x, y = extended_gcd(a1, a2)
    lcm = (a1 * a2) // g
    
    
    count = (R - first_val) // lcm + 1
    
    print(count)

solve()