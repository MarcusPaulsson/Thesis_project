def solve():
  n, a, b, p, q = map(int, input().split())

  red_count = n // a
  blue_count = n // b
  
  lcm = (a * b) // gcd(a, b)
  
  both_count = n // lcm
  
  red_only = red_count - both_count
  blue_only = blue_count - both_count
  
  total_chocolates = red_only * p + blue_only * q + both_count * max(p, q)
  
  print(total_chocolates)

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

solve()