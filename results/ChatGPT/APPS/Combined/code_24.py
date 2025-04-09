def can_alice_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # right, down, diagonal down-right, diagonal down-left
    n = 10

    def count_consecutive_xs(x, y, dx, dy):
        count = 0
        while 0 <= x < n and 0 <= y < n and board[x][y] == 'X':
            count += 1
            x += dx
            y += dy
        return count

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                board[i][j] = 'X'  # Temporarily place an 'X'
                
                for dx, dy in directions:
                    # Count in both directions
                    total_count = 1  # Starting with the placed 'X'
                    total_count += count_consecutive_xs(i + dx, j + dy, dx, dy)  # Positive direction
                    total_count += count_consecutive_xs(i - dx, j - dy, -dx, -dy)  # Negative direction
                    
                    if total_count >= 5:
                        return "YES"
                
                board[i][j] = '.'  # Remove the temporary 'X'

    return "NO"

# Read the input
board = [list(input().strip()) for _ in range(10)]
print(can_alice_win(board))