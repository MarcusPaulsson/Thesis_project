n, m = map(int, input().split())

if m >= n:
  l = 0
  r = 2 * 10**9
  ans = 0
  while l <= r:
    mid = (l + r) // 2
    if n - (mid * (mid + 1)) // 2 <= 0:
      ans = mid
      r = mid - 1
    else:
      l = mid + 1
  print(ans)
else:
  k = n // m
  n -= k * (k + 1) // 2
  if n <= 0:
    ans = k
    print(ans)
  else:
    l = 0
    r = 2 * 10**9
    ans = 0
    while l <= r:
      mid = (l + r) // 2
      if n - (mid * (mid + 1)) // 2 <= 0:
        ans = mid
        r = mid - 1
      else:
        l = mid + 1
    print(k + ans)