def solve():
    board = [list(input()) for _ in range(10)]

    def check_win(board):
        # Check horizontal
        for row in board:
            for i in range(6):
                if row[i] == 'X' and row[i+1] == 'X' and row[i+2] == 'X' and row[i+3] == 'X' and row[i+4] == 'X':
                    return True

        # Check vertical
        for col in range(10):
            for i in range(6):
                if board[i][col] == 'X' and board[i+1][col] == 'X' and board[i+2][col] == 'X' and board[i+3][col] == 'X' and board[i+4][col] == 'X':
                    return True

        # Check diagonal (top-left to bottom-right)
        for i in range(6):
            for j in range(6):
                if board[i][j] == 'X' and board[i+1][j+1] == 'X' and board[i+2][j+2] == 'X' and board[i+3][j+3] == 'X' and board[i+4][j+4] == 'X':
                    return True

        # Check diagonal (top-right to bottom-left)
        for i in range(6):
            for j in range(4, 10):
                if board[i][j] == 'X' and board[i+1][j-1] == 'X' and board[i+2][j-2] == 'X' and board[i+3][j-3] == 'X' and board[i+4][j-4] == 'X':
                    return True

        return False

    for r in range(10):
        for c in range(10):
            if board[r][c] == '.':
                temp_board = [row[:] for row in board]
                temp_board[r][c] = 'X'
                if check_win(temp_board):
                    print('YES')
                    return

    print('NO')

solve()