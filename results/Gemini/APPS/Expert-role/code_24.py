def solve():
    board = []
    for _ in range(10):
        board.append(list(input()))

    def check_win(new_board):
        for i in range(10):
            for j in range(10):
                if new_board[i][j] == 'X':
                    # Check horizontal
                    if j <= 5 and all(new_board[i][j + k] == 'X' for k in range(5)):
                        return True
                    # Check vertical
                    if i <= 5 and all(new_board[i + k][j] == 'X' for k in range(5)):
                        return True
                    # Check diagonal (top-left to bottom-right)
                    if i <= 5 and j <= 5 and all(new_board[i + k][j + k] == 'X' for k in range(5)):
                        return True
                    # Check diagonal (top-right to bottom-left)
                    if i <= 5 and j >= 4 and all(new_board[i + k][j - k] == 'X' for k in range(5)):
                        return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                temp_board = [row[:] for row in board]
                temp_board[i][j] = 'X'
                if check_win(temp_board):
                    print("YES")
                    return

    print("NO")

solve()