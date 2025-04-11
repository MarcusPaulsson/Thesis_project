def can_win_in_one_turn(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # horizontal, vertical, diagonal /
    
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                # Temporarily place 'X' in the empty cell
                board[i][j] = 'X'
                
                for dx, dy in directions:
                    count = 1
                    
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
                
                # Restore the empty cell
                board[i][j] = '.'
    
    return "NO"

# Read the board input
board = [input().strip() for _ in range(10)]
print(can_win_in_one_turn(board))