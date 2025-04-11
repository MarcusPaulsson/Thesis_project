def solve():
  n = int(input())
  
  if n == 0:
    print(0, 0)
    return
  
  l, r = 0, 2000000000
  k = 0
  while l <= r:
    mid = (l + r) // 2
    if 3 * mid * (mid + 1) <= n:
      k = mid
      l = mid + 1
    else:
      r = mid - 1
      
  rem = n - 3 * k * (k + 1)
  
  if rem <= k + 1:
    x = 2 * (rem - (k + 1))
    y = 2 * k
  elif rem <= 2 * (k + 1):
    x = -2 * (k + 1) + (rem - (k + 1)) * 2
    y = 2 * k - 2 * (rem - (k + 1))
  elif rem <= 3 * (k + 1):
    x = -2 * (rem - 2 * (k + 1))
    y = -2 * k + 2 * (rem - 2 * (k + 1))
  elif rem <= 4 * (k + 1):
    x = 2 * (rem - 3 * (k + 1))
    y = -2 * k
  elif rem <= 5 * (k + 1):
    x = 2 * (k + 1) - 2 * (rem - 4 * (k + 1))
    y = -2 * k + 2 * (rem - 4 * (k + 1))
  else:
    x = 2 * (k + 1) - 2 * (rem - 5 * (k + 1))
    y = 2 * k - 2 * (rem - 5 * (k + 1))
  
  print(x, y)
  
solve()