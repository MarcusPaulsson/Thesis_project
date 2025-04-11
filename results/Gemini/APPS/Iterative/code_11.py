def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

n, a, b, p, q = map(int, input().split())

red_count = n // a
blue_count = n // b
both_count = n // lcm(a, b)

total_chocolates = 0

if p > q:
    total_chocolates += red_count * p + (blue_count - both_count) * q
else:
    total_chocolates += blue_count * q + (red_count - both_count) * p

print(total_chocolates)