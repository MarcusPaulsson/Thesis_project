def solve():
    board = []
    for _ in range(10):
        board.append(list(input()))

    def check_win(board):
        n = 10
        # Check horizontal
        for r in range(n):
            for c in range(n - 4):
                if all(board[r][c + i] == 'X' for i in range(5)):
                    return True

        # Check vertical
        for c in range(n):
            for r in range(n - 4):
                if all(board[r + i][c] == 'X' for i in range(5)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for r in range(n - 4):
            for c in range(n - 4):
                if all(board[r + i][c + i] == 'X' for i in range(5)):
                    return True

        # Check diagonal (top-right to bottom-left)
        for r in range(n - 4):
            for c in range(4, n):
                if all(board[r + i][c - i] == 'X' for i in range(5)):
                    return True

        return False

    for r in range(10):
        for c in range(10):
            if board[r][c] == '.':
                board[r][c] = 'X'
                if check_win(board):
                    print("YES")
                    return
                board[r][c] = '.'

    print("NO")

solve()