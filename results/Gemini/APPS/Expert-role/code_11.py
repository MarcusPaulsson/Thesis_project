import math

def solve():
    n, a, b, p, q = map(int, input().split())
    
    red_count = n // a
    blue_count = n // b
    
    lcm = (a * b) // math.gcd(a, b)
    
    both_count = n // lcm
    
    red_only = red_count - both_count
    blue_only = blue_count - both_count
    
    total_chocolates = red_only * p + blue_only * q
    
    if p > q:
        total_chocolates += both_count * p
    else:
        total_chocolates += both_count * q
        
    print(total_chocolates)

solve()