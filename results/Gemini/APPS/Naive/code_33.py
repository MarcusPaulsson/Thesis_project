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

    k = (x * a1 + b1)
    
    
    first = k % lcm
    if first < 0:
        first += lcm
    
    
    start = first
    
    while start < L:
        start += lcm
        
    count = 0
    while start <= R:
        count += 1
        start += lcm
        
    print(count)

solve()