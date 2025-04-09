def can_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # horizontal, vertical, diagonal down-right, diagonal down-left
    n = 10

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                # Simulate placing 'X' at (i, j)
                board[i][j] = 'X'
                
                # Check for winning conditions
                for dx, dy in directions:
                    count = 1  # Start with the current position

                    # Check in the positive direction
                    x, y = i + dx, j + dy
                    while 0 <= x < n and 0 <= y < n and board[x][y] == 'X':
                        count += 1
                        x += dx
                        y += dy

                    # Check in the negative direction
                    x, y = i - dx, j - dy
                    while 0 <= x < n and 0 <= y < n and board[x][y] == 'X':
                        count += 1
                        x -= dx
                        y -= dy

                    # If count reaches 5, Alice wins
                    if count >= 5:
                        return 'YES'
                
                # Reset the cell back to empty
                board[i][j] = '.'

    return 'NO'

# Reading input
board = [input().strip() for _ in range(10)]
print(can_win(board))