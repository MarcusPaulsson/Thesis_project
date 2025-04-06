def solve():
    board = [input() for _ in range(10)]

    def check_win(board):
        # Horizontal
        for row in board:
            for i in range(len(row) - 4):
                if all(row[i+j] == 'X' for j in range(5)):
                    return True

        # Vertical
        for col in range(10):
            for i in range(10 - 4):
                if all(board[i+j][col] == 'X' for j in range(5)):
                    return True

        # Diagonal (top-left to bottom-right)
        for row in range(10 - 4):
            for col in range(10 - 4):
                if all(board[row+j][col+j] == 'X' for j in range(5)):
                    return True

        # Diagonal (top-right to bottom-left)
        for row in range(10 - 4):
            for col in range(4, 10):
                if all(board[row+j][col-j] == 'X' for j in range(5)):
                    return True

        return False

    for row in range(10):
        for col in range(10):
            if board[row][col] == '.':
                new_board = [list(row_str) for row_str in board]
                new_board[row][col] = 'X'
                new_board_str = ["".join(row_list) for row_list in new_board]
                if check_win(new_board_str):
                    print('YES')
                    return

    print('NO')

solve()