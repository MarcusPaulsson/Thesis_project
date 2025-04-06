def extended_gcd(a, b):
  """
  Extended Euclidean algorithm to find the greatest common divisor (GCD) of a and b,
  as well as coefficients x and y such that ax + by = gcd(a, b).

  Args:
    a: An integer.
    b: An integer.

  Returns:
    A tuple (gcd, x, y) where:
      gcd: The greatest common divisor of a and b.
      x: An integer coefficient such that ax + by = gcd.
      y: An integer coefficient such that ax + by = gcd.
  """
  if a == 0:
    return (b, 0, 1)

  gcd, x1, y1 = extended_gcd(b % a, a)

  x = y1 - (b // a) * x1
  y = x1

  return (gcd, x, y)


def solve():
  """
  Reads input, calculates the number of integers that satisfy the given conditions,
  and prints the result.
  """
  a1, b1, a2, b2, L, R = map(int, input().split())

  # Find the smallest x such that x = a1*k + b1 = a2*l + b2 for some k, l >= 0.
  # This is equivalent to solving a1*k - a2*l = b2 - b1.
  diff = b2 - b1
  gcd, x, y = extended_gcd(a1, a2)

  if diff % gcd != 0:
    print(0)
    return

  x *= (diff // gcd)
  y *= (diff // gcd)

  # Find the general solution for k and l:
  # k = x + (a2/gcd)*t
  # l = y + (a1/gcd)*t
  # x = a1*k + b1 = a1*(x + (a2/gcd)*t) + b1

  # Find the smallest value of t such that k >= 0 and l >= 0.
  t1 = -x * gcd // a2
  if (-x * gcd) % a2 != 0:
    t1 -= 1
  
  t2 = -y * gcd // a1
  if (-y * gcd) % a1 != 0:
    t2 -= 1
  
  t = max(t1, t2)

  k = x + (a2 // gcd) * t
  l = y + (a1 // gcd) * t

  start_x = a1 * k + b1
  
  if start_x < L:
    add = (L - start_x + (a1 * a2 // gcd) - 1) // (a1 * a2 // gcd)
    start_x += add * (a1 * a2 // gcd)
  
  if start_x > R:
    print(0)
    return

  count = (R - start_x) // (a1 * a2 // gcd) + 1
  print(count)


if __name__ == "__main__":
  solve()