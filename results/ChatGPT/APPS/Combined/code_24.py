def can_alice_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # right, down, diagonal right-down, diagonal left-down
    n = 10  # board size

    def check_win(x, y):
        for dx, dy in directions:
            count = 1  # Start counting from the current position
            # Check in the positive direction
            count += count_streak(x, y, dx, dy)
            # Check in the negative direction
            count += count_streak(x, y, -dx, -dy)
            
            if count >= 5:
                return True
        return False

    def count_streak(x, y, dx, dy):
        count = 0
        for step in range(1, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                count += 1
            else:
                break
        return count

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Place a cross temporarily
                if check_win(i, j):
                    return 'YES'
                board[i][j] = '.'  # Reset the cell

    return 'NO'


# Read input
board = [input().strip() for _ in range(10)]
print(can_alice_win(board))