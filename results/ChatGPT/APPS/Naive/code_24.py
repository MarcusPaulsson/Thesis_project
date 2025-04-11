def can_win_in_one_turn(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal down-right, diagonal down-left
    n = 10

    def check_win(x, y):
        for dx, dy in directions:
            count = 1  # Count the current position
            # Check in the positive direction
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                    count += 1
                else:
                    break
            # Check in the negative direction
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Place a cross
                if check_win(i, j):
                    return "YES"
                board[i][j] = '.'  # Undo the move
    return "NO"

# Read input
board = [input().strip() for _ in range(10)]
print(can_win_in_one_turn(board))