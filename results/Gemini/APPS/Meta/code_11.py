def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve():
    n, a, b, p, q = map(int, input().split())
    
    red_count = n // a
    blue_count = n // b
    both_count = n // lcm(a, b)
    
    if p > q:
        result = red_count * p + (blue_count - both_count) * q
    else:
        result = blue_count * q + (red_count - both_count) * p
        
    print(result)

solve()