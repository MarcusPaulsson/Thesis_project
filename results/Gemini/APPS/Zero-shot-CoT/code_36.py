def solve():
  n = int(input())

  if n == 0:
    print(0, 0)
    return

  l, r = 0, 10**9
  k = 0
  while l <= r:
    mid = (l + r) // 2
    if 3 * mid * (mid + 1) >= n:
      k = mid
      r = mid - 1
    else:
      l = mid + 1

  n -= 3 * k * (k - 1)
  k -= 1 if k > 0 else 0

  x, y = 2 * k + 1, 0
  
  if n <= 0:
      x, y = 0, 0
  elif n <= k + 1:
    x += 2 * (n - (k + 1))
    y += 2 * (n - (k + 1))
  elif n <= 2 * (k + 1):
    x += 2 * (k + 1 - (n))
    y += 2 * (k + 1)
  elif n <= 3 * (k + 1):
    x += -2 * (n - 2 * (k + 1))
    y += 2 * (k + 1)
  elif n <= 4 * (k + 1):
    x += -2 * (k + 1)
    y += -2 * (n - 3 * (k + 1))
  elif n <= 5 * (k + 1):
    x += -2 * (4 * (k + 1) - n)
    y += -2 * (k + 1)
  else:
    x += 2 * (n - 5 * (k + 1))
    y += -2 * (k + 1)

  print(x, y)

solve()