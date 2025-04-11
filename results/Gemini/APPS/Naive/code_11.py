def solve():
    n, a, b, p, q = map(int, input().split())

    red_count = n // a
    blue_count = n // b
    
    lcm_val = (a * b) // gcd(a, b)
    
    both_count = n // lcm_val

    red_only = red_count - both_count
    blue_only = blue_count - both_count

    if p > q:
        total_chocolates = (red_only * p) + (both_count * p) + (blue_only * q)
    else:
        total_chocolates = (red_only * p) + (both_count * q) + (blue_only * q)

    print(total_chocolates)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve()