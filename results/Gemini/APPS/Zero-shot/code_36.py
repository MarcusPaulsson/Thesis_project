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
  
  x, y = 2 * k, 0
  
  if n <= k:
    x -= 2 * n
    print(x, y)
  elif n <= 2 * k:
    x -= 2 * k
    y += 2 * (n - k)
    print(x, y)
  elif n <= 3 * k:
    x -= 2 * (2 * k - n)
    y += 2 * k
    print(x, y)
  elif n <= 4 * k:
    x += 2 * (n - 3 * k)
    y -= 2 * (4 * k - n)
    print(x, y)
  elif n <= 5 * k:
    x += 2 * k
    y -= 2 * k
    x += 2 * (5 * k - n)
    print(x, y)
  else:
    x += 2 * (6 * k - n)
    print(x, y)

solve()