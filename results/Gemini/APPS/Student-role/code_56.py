def solve():
  n, k = map(int, input().split())
  
  grid = [['0'] * n for _ in range(n)]
  
  row = 0
  col = 0
  
  for _ in range(k):
    grid[row][col] = '1'
    row = (row + 1) % n
    col = (col + 1) % n
    if grid[row][col] == '1':
      col = (col + 1) % n
  
  row_sums = [0] * n
  col_sums = [0] * n
  
  for i in range(n):
    for j in range(n):
      if grid[i][j] == '1':
        row_sums[i] += 1
        col_sums[j] += 1
  
  f_a = (max(row_sums) - min(row_sums))**2 + (max(col_sums) - min(col_sums))**2
  
  print(f_a)
  for row_arr in grid:
    print("".join(row_arr))

t = int(input())
for _ in range(t):
  solve()