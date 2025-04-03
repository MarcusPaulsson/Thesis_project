def can_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    def check_line(x, y, dx, dy):
        count = 0
        for step in range(-4, 1):  # Check in both directions
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
            else:
                count = 0
            
            if count >= 5:
                return True
        return False

    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                # Temporarily place 'X' to check for a win
                board[i][j] = 'X'
                for dx, dy in directions:
                    if check_line(i, j, dx, dy):
                        return "YES"
                # Reset the cell back to empty
                board[i][j] = '.'
    
    return "NO"

# Read the input
board = [input().strip() for _ in range(10)]
print(can_win(board))