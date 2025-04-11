def solve():
    board = []
    for _ in range(10):
        board.append(list(input()))

    def check_win(board):
        for i in range(10):
            for j in range(10):
                if board[i][j] == 'X':
                    # Check horizontal
                    if j + 4 < 10:
                        if all(board[i][j+k] == 'X' for k in range(5)):
                            return True
                    # Check vertical
                    if i + 4 < 10:
                        if all(board[i+k][j] == 'X' for k in range(5)):
                            return True
                    # Check diagonal (top-left to bottom-right)
                    if i + 4 < 10 and j + 4 < 10:
                        if all(board[i+k][j+k] == 'X' for k in range(5)):
                            return True
                    # Check diagonal (top-right to bottom-left)
                    if i + 4 < 10 and j - 4 >= 0:
                        if all(board[i+k][j-k] == 'X' for k in range(5)):
                            return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                board[i][j] = 'X'
                if check_win(board):
                    print('YES')
                    return
                board[i][j] = '.'

    print('NO')

solve()