def solve():
  n, m = map(int, input().split())
  count = 0
  for x in range(1, n + 1):
    for y in range(1, m + 1):
      if (x + y) % 5 == 0:
        count += 1
  print(count)

solve()