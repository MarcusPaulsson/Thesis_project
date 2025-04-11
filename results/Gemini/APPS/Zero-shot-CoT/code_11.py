def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def lcm(a, b):
  return (a * b) // gcd(a, b)

n, a, b, p, q = map(int, input().split())

red_count = n // a
blue_count = n // b
common_count = n // lcm(a, b)

red_only = red_count - common_count
blue_only = blue_count - common_count

total_chocolates = red_only * p + blue_only * q

if p > q:
  total_chocolates += common_count * p
else:
  total_chocolates += common_count * q

print(total_chocolates)