def solve():
    board = []
    for _ in range(10):
        board.append(list(input()))

    def check_win(board):
        def check_horizontal(board):
            for row in board:
                for i in range(len(row) - 4):
                    if all(row[i + j] == 'X' for j in range(5)):
                        return True
            return False

        def check_vertical(board):
            for col in range(len(board[0])):
                for i in range(len(board) - 4):
                    if all(board[i + j][col] == 'X' for j in range(5)):
                        return True
            return False

        def check_diagonal(board):
            for row in range(len(board) - 4):
                for col in range(len(board[0]) - 4):
                    if all(board[row + j][col + j] == 'X' for j in range(5)):
                        return True

            for row in range(len(board) - 4):
                for col in range(4, len(board[0])):
                    if all(board[row + j][col - j] == 'X' for j in range(5)):
                        return True
            return False

        return check_horizontal(board) or check_vertical(board) or check_diagonal(board)

    for r in range(10):
        for c in range(10):
            if board[r][c] == '.':
                board[r][c] = 'X'
                if check_win(board):
                    print('YES')
                    return
                board[r][c] = '.'
    print('NO')

solve()