def can_win(matrix):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # down, right, down-right, down-left

    def check_win(x, y):
        for dx, dy in directions:
            count = 1  # Start with the current position
            # Check in the positive direction
            nx, ny = x + dx, y + dy
            while 0 <= nx < 10 and 0 <= ny < 10 and matrix[nx][ny] == 'X':
                count += 1
                nx += dx
                ny += dy
            # Check in the negative direction
            nx, ny = x - dx, y - dy
            while 0 <= nx < 10 and 0 <= ny < 10 and matrix[nx][ny] == 'X':
                count += 1
                nx -= dx
                ny -= dy
            if count >= 5:
                return True
        return False

    for i in range(10):
        for j in range(10):
            if matrix[i][j] == '.':
                matrix[i][j] = 'X'  # Try placing a cross
                if check_win(i, j):
                    return 'YES'
                matrix[i][j] = '.'  # Reset the cell back
    return 'NO'


# Read input matrix
matrix = [input().strip() for _ in range(10)]
print(can_win(matrix))