def can_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal down-right, diagonal down-left
    n = 10

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                # Temporarily place 'X' in the empty cell
                board[i][j] = 'X'
                
                for dx, dy in directions:
                    count = 1
                    
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
                    
                    if count >= 5:
                        return "YES"
                
                # Remove the temporary 'X'
                board[i][j] = '.'

    return "NO"

# Read input
board = [input().strip() for _ in range(10)]
print(can_win(board))