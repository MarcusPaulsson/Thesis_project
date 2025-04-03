def extended_gcd(a, b):
  if a == 0:
    return b, 0, 1
  d, x1, y1 = extended_gcd(b % a, a)
  x = y1 - (b // a) * x1
  y = x1
  return d, x, y


def crt(a1, m1, a2, m2):
  g, x, y = extended_gcd(m1, m2)
  if (a2 - a1) % g != 0:
    return None, None
  else:
    lcm = m1 * m2 // g
    result = (a1 + (a2 - a1) // g * x % (m2 // g) * m1) % lcm
    return result, lcm


a1, b1, a2, b2, L, R = map(int, input().split())

result, lcm = crt(b1 % a1, a1, b2 % a2, a2)

if result is None:
  print(0)
else:
  lcm_val = lcm
  first_val = result
  
  start = max(L, max(b1, b2))
  
  if first_val < start:
    k = (start - first_val + lcm_val - 1) // lcm_val
    first_val += k * lcm_val
    
  if first_val > R:
    print(0)
  else:
    count = (R - first_val) // lcm_val + 1
    print(count)