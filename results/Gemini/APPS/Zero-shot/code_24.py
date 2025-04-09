def solve():
  board = [input() for _ in range(10)]

  def check_win(board):
    for i in range(10):
      for j in range(10):
        if board[i][j] == 'X':
          # Check horizontal
          if j <= 5 and all(board[i][j + k] == 'X' for k in range(5)):
            return True
          # Check vertical
          if i <= 5 and all(board[i + k][j] == 'X' for k in range(5)):
            return True
          # Check diagonal (top-left to bottom-right)
          if i <= 5 and j <= 5 and all(board[i + k][j + k] == 'X' for k in range(5)):
            return True
          # Check diagonal (top-right to bottom-left)
          if i <= 5 and j >= 4 and all(board[i + k][j - k] == 'X' for k in range(5)):
            return True
    return False

  for i in range(10):
    for j in range(10):
      if board[i][j] == '.':
        new_board = [list(row) for row in board]
        new_board[i][j] = 'X'
        new_board = ["".join(row) for row in new_board]
        if check_win(new_board):
          print('YES')
          return

  print('NO')

solve()