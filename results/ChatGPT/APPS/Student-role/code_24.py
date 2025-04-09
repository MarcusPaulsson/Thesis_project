def can_win(field):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Vertical, Horizontal, Diagonal /
    
    for i in range(10):
        for j in range(10):
            if field[i][j] == '.':
                # Try placing 'X' in the empty cell
                for di, dj in directions:
                    count = 1  # Count the placed 'X'
                    
                    # Check in the positive direction
                    ni, nj = i + di, j + dj
                    while 0 <= ni < 10 and 0 <= nj < 10 and field[ni][nj] == 'X':
                        count += 1
                        ni += di
                        nj += dj
                    
                    # Check in the negative direction
                    ni, nj = i - di, j - dj
                    while 0 <= ni < 10 and 0 <= nj < 10 and field[ni][nj] == 'X':
                        count += 1
                        ni -= di
                        nj -= dj
                    
                    # Check if Alice can win
                    if count >= 5:
                        return "YES"
    
    return "NO"

# Reading the 10x10 game field input
field = [input().strip() for _ in range(10)]
print(can_win(field))