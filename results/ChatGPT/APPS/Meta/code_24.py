def can_alice_win(board):
    # Directions for horizontal, vertical, and two diagonals
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    def check_win(x, y):
        # Check all 4 directions
        for dx, dy in directions:
            count = 1  # Start with the newly placed cross
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

    # Try placing 'X' in every empty cell and check for a win
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Place a cross
                if check_win(i, j):
                    return "YES"
                board[i][j] = '.'  # Remove the cross
    return "NO"

# Input reading
board = [input().strip() for _ in range(10)]
print(can_alice_win(board))