def solve():
  n = int(input())
  q = list(map(int, input().split()))

  p = [0] * n
  used = [False] * (n + 1)

  p[0] = q[0]
  used[p[0]] = True

  for i in range(1, n):
    if q[i] > q[i-1]:
      p[i] = q[i]
      used[p[i]] = True
    else:
      found = False
      for j in range(1, q[i]):
        if not used[j]:
          p[i] = j
          used[j] = True
          found = True
          break
      if not found:
        print("-1")
        return

  if len(set(p)) != n:
    print("-1")
    return

  print(*p)


t = int(input())
for _ in range(t):
  solve()