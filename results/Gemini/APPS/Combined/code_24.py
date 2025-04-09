def check_win(board):
    """Checks if there is a winning line of 5 or more 'X's on the board."""
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'X':
                # Check horizontal
                if c + 4 < n and all(board[r][c + i] == 'X' for i in range(5)):
                    return True
                # Check vertical
                if r + 4 < n and all(board[r + i][c] == 'X' for i in range(5)):
                    return True
                # Check diagonal (top-left to bottom-right)
                if r + 4 < n and c + 4 < n and all(board[r + i][c + i] == 'X' for i in range(5)):
                    return True
                # Check diagonal (top-right to bottom-left)
                if r + 4 < n and c - 4 >= 0 and all(board[r + i][c - i] == 'X' for i in range(5)):
                    return True
    return False


def solve():
    """Reads the board, tries placing 'X' in each empty cell, and checks for a win."""
    board = []
    for _ in range(10):
        board.append(list(input()))

    for r in range(10):
        for c in range(10):
            if board[r][c] == '.':
                board[r][c] = 'X'
                if check_win(board):
                    print('YES')
                    return
                board[r][c] = '.'  # Backtrack

    print('NO')


if __name__ == "__main__":
    solve()