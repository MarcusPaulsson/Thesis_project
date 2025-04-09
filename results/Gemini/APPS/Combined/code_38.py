def solve():
  n, l = map(int, input().split())
  kefa = list(map(int, input().split()))
  sasha = list(map(int, input().split()))

  for shift in range(l):
    match = True
    for i in range(n):
      if (kefa[i] - sasha[0] + l) % l != (sasha[i] - sasha[0] + l) % l:
        match = False
        break
    if match:
      print("YES")
      return

  print("NO")

solve()