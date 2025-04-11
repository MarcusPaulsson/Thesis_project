def can_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    def check_win(x, y):
        for dx, dy in directions:
            count = 1
            
            # Check in the positive direction
            nx, ny = x + dx, y + dy
            while 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
                nx += dx
                ny += dy
            
            # Check in the negative direction
            nx, ny = x - dx, y - dy
            while 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
                nx -= dx
                ny -= dy
            
            if count >= 5:
                return True
        return False
    
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Place the cross
                if check_win(i, j):
                    return "YES"
                board[i][j] = '.'  # Revert back
    return "NO"

# Read input
board = [input().strip() for _ in range(10)]
print(can_win(board))