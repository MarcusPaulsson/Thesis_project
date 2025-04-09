def solve():
  n = int(input())
  a = list(map(int, input().split()))

  pos_min = a.index(1)
  pos_max = a.index(n)

  print(max(pos_max, pos_min, n - 1 - pos_min, n - 1 - pos_max))

solve()