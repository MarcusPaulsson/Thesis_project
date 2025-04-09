def can_win(board):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # horizontal, vertical, diagonal down-right, diagonal down-left
    
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                # Temporarily place an 'X' in the empty cell
                board[i][j] = 'X'
                
                # Check for a winning line
                for dx, dy in directions:
                    count = 1  # count the placed 'X'
                    
                    # Check in the positive direction
                    x, y = i + dx, j + dy
                    while 0 <= x < 10 and 0 <= y < 10 and board[x][y] == 'X':
                        count += 1
                        x += dx
                        y += dy
                    
                    # Check in the negative direction
                    x, y = i - dx, j - dy
                    while 0 <= x < 10 and 0 <= y < 10 and board[x][y] == 'X':
                        count += 1
                        x -= dx
                        y -= dy
                    
                    if count >= 5:
                        return "YES"
                
                # Revert the temporary placement
                board[i][j] = '.'
    
    return "NO"

# Read input
board = [input().strip() for _ in range(10)]
print(can_win(board))