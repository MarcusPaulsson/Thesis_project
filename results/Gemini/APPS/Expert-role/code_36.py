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
  
  n -= 3 * k * (k - 1) if k > 0 else 0

  if 1 <= n <= k:
    x = 2 * k - n
    y = 2 * n
  elif k + 1 <= n <= 2 * k:
    x = k - 2 * (n - k)
    y = 2 * k
  elif 2 * k + 1 <= n <= 3 * k:
    x = -k - (n - 2 * k)
    y = 2 * k - 2 * (n - 2 * k)
  elif 3 * k + 1 <= n <= 4 * k:
    x = -2 * k + (n - 3 * k)
    y = -2 * (n - 3 * k)
  elif 4 * k + 1 <= n <= 5 * k:
    x = -k + 2 * (n - 4 * k)
    y = -2 * k
  else:
    x = k + (n - 5 * k)
    y = -2 * k + 2 * (n - 5 * k)
  
  print(x, y)

solve()