def check_win(board, player):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                # Check horizontal
                if j + 4 < n and all(board[i][j + k] == player for k in range(5)):
                    return True
                # Check vertical
                if i + 4 < n and all(board[i + k][j] == player for k in range(5)):
                    return True
                # Check diagonal (down-right)
                if i + 4 < n and j + 4 < n and all(board[i + k][j + k] == player for k in range(5)):
                    return True
                # Check diagonal (down-left)
                if i + 4 < n and j - 4 >= 0 and all(board[i + k][j - k] == player for k in range(5)):
                    return True
    return False

board = [input().strip() for _ in range(10)]
if check_win(board, 'X'):
    print('YES')
else:
    print('NO')