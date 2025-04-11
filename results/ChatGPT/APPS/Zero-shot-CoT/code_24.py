def can_win(matrix):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal right, diagonal left
    n = 10

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '.':
                # Temporarily place 'X' in the empty cell
                matrix[i][j] = 'X'
                
                # Check for a win in all directions
                for dx, dy in directions:
                    count = 1  # Count the current placed 'X'
                    
                    # Check in the positive direction
                    x, y = i + dx, j + dy
                    while 0 <= x < n and 0 <= y < n and matrix[x][y] == 'X':
                        count += 1
                        x += dx
                        y += dy
                    
                    # Check in the negative direction
                    x, y = i - dx, j - dy
                    while 0 <= x < n and 0 <= y < n and matrix[x][y] == 'X':
                        count += 1
                        x -= dx
                        y -= dy
                    
                    # If we have 5 or more in a row, Alice wins
                    if count >= 5:
                        return "YES"
                
                # Remove the temporary 'X'
                matrix[i][j] = '.'

    return "NO"

# Read the input matrix
matrix = [list(input().strip()) for _ in range(10)]
print(can_win(matrix))