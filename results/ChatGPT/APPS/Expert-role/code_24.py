def can_alice_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # right, down, diagonal down-right, diagonal down-left
    size = 10
    
    def check_win(x, y):
        for dx, dy in directions:
            count = 1
            
            # Check in the positive direction
            nx, ny = x + dx, y + dy
            while 0 <= nx < size and 0 <= ny < size and board[nx][ny] == 'X':
                count += 1
                nx += dx
                ny += dy
            
            # Check in the negative direction
            nx, ny = x - dx, y - dy
            while 0 <= nx < size and 0 <= ny < size and board[nx][ny] == 'X':
                count += 1
                nx -= dx
                ny -= dy
            
            if count >= 5:
                return True
        return False

    for i in range(size):
        for j in range(size):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Simulate Alice's move
                if check_win(i, j):
                    return "YES"
                board[i][j] = '.'  # Undo the move

    return "NO"

# Read the input
board = [input().strip() for _ in range(10)]
print(can_alice_win(board))