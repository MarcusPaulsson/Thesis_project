def solve():
  n, k, t = map(int, input().split())

  if t <= k:
    print(t)
  elif t <= n:
    print(k)
  else:
    print(max(0, k - (t - n)))

solve()