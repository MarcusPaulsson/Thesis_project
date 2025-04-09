def can_win(matrix):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    def check_direction(x, y, dx, dy):
        count = 0
        for i in range(-4, 1):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < 10 and 0 <= ny < 10 and matrix[nx][ny] == 'X':
                count += 1
            else:
                count = 0
            if count >= 4:
                return True
        return False

    for i in range(10):
        for j in range(10):
            if matrix[i][j] == '.':
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy):
                        return 'YES'
    return 'NO'

# Read input
matrix = [input().strip() for _ in range(10)]
print(can_win(matrix))