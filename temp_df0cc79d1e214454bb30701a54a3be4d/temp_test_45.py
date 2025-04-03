def solve():
  x = int(input())
  count = 0
  staircase_size = 1
  while True:
    cells_needed = staircase_size * (staircase_size + 1) // 2
    if cells_needed <= x:
      x -= cells_needed
      count += 1
      staircase_size = staircase_size * 2 + 1
    else:
      break
  print(count)

t = int(input())
for _ in range(t):
  solve()