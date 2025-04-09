def check_win(board):
    """Checks if there is a 5-in-a-row win for 'X' on the board.

    Args:
        board: A list of strings representing the game board.

    Returns:
        True if there is a win, False otherwise.
    """
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                # Check horizontal
                if j <= n - 5 and all(board[i][j + k] == 'X' for k in range(5)):
                    return True
                # Check vertical
                if i <= n - 5 and all(board[i + k][j] == 'X' for k in range(5)):
                    return True
                # Check diagonal (top-left to bottom-right)
                if i <= n - 5 and j <= n - 5 and all(board[i + k][j + k] == 'X' for k in range(5)):
                    return True
                # Check diagonal (top-right to bottom-left)
                if i <= n - 5 and j >= 4 and all(board[i + k][j - k] == 'X' for k in range(5)):
                    return True
    return False


def solve():
    """Reads the board, checks for a winning move for Alice, and prints the result."""
    board = [input() for _ in range(10)]

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


if __name__ == "__main__":
    solve()