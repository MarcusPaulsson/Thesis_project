def solve():
  n, m = map(int, input().split())
  customers = []
  for _ in range(n):
    customers.append(list(map(int, input().split())))

  low = m
  high = m
  prev_time = 0

  for t, l, h in customers:
    time_diff = t - prev_time
    low -= time_diff
    high += time_diff

    if high < l or low > h:
      print("NO")
      return

    low = max(low, l)
    high = min(high, h)
    prev_time = t

  print("YES")


q = int(input())
for _ in range(q):
  solve()