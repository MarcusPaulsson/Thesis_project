def solve():
    board = []
    for _ in range(10):
        board.append(list(input()))

    def check_win(board):
        # Check horizontal
        for row in board:
            for i in range(len(row) - 4):
                if row[i] == 'X' and row[i+1] == 'X' and row[i+2] == 'X' and row[i+3] == 'X' and row[i+4] == 'X':
                    return True

        # Check vertical
        for col in range(10):
            for i in range(10 - 4):
                if board[i][col] == 'X' and board[i+1][col] == 'X' and board[i+2][col] == 'X' and board[i+3][col] == 'X' and board[i+4][col] == 'X':
                    return True

        # Check diagonal (top-left to bottom-right)
        for i in range(10 - 4):
            for j in range(10 - 4):
                if board[i][j] == 'X' and board[i+1][j+1] == 'X' and board[i+2][j+2] == 'X' and board[i+3][j+3] == 'X' and board[i+4][j+4] == 'X':
                    return True

        # Check diagonal (top-right to bottom-left)
        for i in range(10 - 4):
            for j in range(4, 10):
                if board[i][j] == 'X' and board[i+1][j-1] == 'X' and board[i+2][j-2] == 'X' and board[i+3][j-3] == 'X' and board[i+4][j-4] == 'X':
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