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
    common_count = n // lcm(a, b)
    
    red_only = red_count - common_count
    blue_only = blue_count - common_count
    
    total_chocolates = 0
    
    if p > q:
        total_chocolates += red_only * p
        total_chocolates += common_count * p
        total_chocolates += blue_only * q
    else:
        total_chocolates += blue_only * q
        total_chocolates += common_count * q
        total_chocolates += red_only * p
    
    print(total_chocolates)

solve()