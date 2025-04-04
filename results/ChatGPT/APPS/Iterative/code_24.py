def can_alice_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal
    
    def count_streaks(x, y, dx, dy):
        count = 0
        for step in range(5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
            else:
                break
        return count
    
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                for dx, dy in directions:
                    total_count = count_streaks(i, j, dx, dy) + count_streaks(i, j, -dx, -dy)
                    if total_count >= 4:  # +1 for the new cross we would place
                        return "YES"
    
    return "NO"

# Read input
board = [input().strip() for _ in range(10)]
if all(len(row) == 10 for row in board):  # Ensure each row has exactly 10 characters
    print(can_alice_win(board))
else:
    print("Input error: Each row must contain exactly 10 characters.")