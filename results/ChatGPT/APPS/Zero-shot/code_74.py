def can_win(matrix):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    def check_win(x, y):
        for dx, dy in directions:
            count = 1
            
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < 10 and 0 <= ny < 10 and matrix[nx][ny] == 'X':
                    count += 1
                else:
                    break
            
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < 10 and 0 <= ny < 10 and matrix[nx][ny] == 'X':
                    count += 1
                else:
                    break
            
            if count >= 5:
                return True
        return False
    
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == '.':
                matrix[i][j] = 'X'
                if check_win(i, j):
                    return 'YES'
                matrix[i][j] = '.'  # Reset the cell back
    
    return 'NO'


# Read input
matrix = [list(input().strip()) for _ in range(10)]
print(can_win(matrix))