def solve():
  grid = []
  for _ in range(10):
    grid.append(list(input()))

  def check_win(grid):
    # Check horizontal
    for row in range(10):
      for col in range(6):
        if all(grid[row][col + i] == 'X' for i in range(5)):
          return True

    # Check vertical
    for col in range(10):
      for row in range(6):
        if all(grid[row + i][col] == 'X' for i in range(5)):
          return True

    # Check diagonal (top-left to bottom-right)
    for row in range(6):
      for col in range(6):
        if all(grid[row + i][col + i] == 'X' for i in range(5)):
          return True

    # Check diagonal (top-right to bottom-left)
    for row in range(6):
      for col in range(4, 10):
        if all(grid[row + i][col - i] == 'X' for i in range(5)):
          return True

    return False

  for row in range(10):
    for col in range(10):
      if grid[row][col] == '.':
        grid[row][col] = 'X'
        if check_win(grid):
          print('YES')
          return
        grid[row][col] = '.'

  print('NO')

solve()