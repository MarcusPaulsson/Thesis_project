def solve():
    board = []
    for _ in range(10):
        board.append(input())

    def check_win(board):
        n = 10
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    # Check horizontal
                    if j + 4 < n and all(board[i][j+k] == 'X' for k in range(5)):
                        return True
                    # Check vertical
                    if i + 4 < n and all(board[i+k][j] == 'X' for k in range(5)):
                        return True
                    # Check diagonal (top-left to bottom-right)
                    if i + 4 < n and j + 4 < n and all(board[i+k][j+k] == 'X' for k in range(5)):
                        return True
                    # Check diagonal (top-right to bottom-left)
                    if i + 4 < n and j - 4 >= 0 and all(board[i+k][j-k] == 'X' for k in range(5)):
                        return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                temp_board = [list(row) for row in board]
                temp_board[i][j] = 'X'
                temp_board = ["".join(row) for row in temp_board]
                if check_win(temp_board):
                    print('YES')
                    return

    print('NO')

solve()