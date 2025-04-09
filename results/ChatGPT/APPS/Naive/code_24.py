def can_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal right, diagonal left
    n = 10

    def check_win(x, y):
        for dx, dy in directions:
            count = 1

            # Check in the positive direction
            nx, ny = x + dx, y + dy
            while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                count += 1
                nx += dx
                ny += dy

            # Check in the negative direction
            nx, ny = x - dx, y - dy
            while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
                count += 1
                nx -= dx
                ny -= dy

            if count >= 5:
                return True
        return False

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Place the cross
                if check_win(i, j):
                    return "YES"
                board[i][j] = '.'  # Remove the cross

    return "NO"

# Read input
board = [input().strip() for _ in range(10)]
print(can_win(board))