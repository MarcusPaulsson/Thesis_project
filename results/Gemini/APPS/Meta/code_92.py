def solve():
  x = float(input())
  for i in range(1, 11):
    for j in range(1, 11):
      if abs(i / j - x) < 1e-7:
        print(i, j)
        return

solve()