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
    x *= (b2 - b1) // g
    y *= (b2 - b1) // g

    lcm = (a1 * a2) // g

    x0 = x
    y0 = y

    k = (L - b1)
    if k % a1 != 0:
      k = (k // a1 + 1) * a1
    else:
      k = k
    
    first_x = -1
    
    for i in range(100000):
      curr_x = a1 * (x0 + (a2 // g) * i) + b1
      if curr_x >= L:
        first_x = curr_x
        break
    
    if first_x == -1:
      for i in range(100000):
        curr_x = a1 * (x0 - (a2 // g) * i) + b1
        if curr_x >= L:
          first_x = curr_x
          break
    
    if first_x == -1:
      print(0)
      return
    
    if first_x > R:
      print(0)
      return

    count = (R - first_x) // lcm + 1
    print(count)

solve()