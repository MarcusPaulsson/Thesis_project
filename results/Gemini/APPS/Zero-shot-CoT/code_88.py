def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def is_palindromic(mat):
        rows = len(mat)
        cols = len(mat[0])
        
        # Check rows
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != mat[rows - 1 - i][j]:
                    return False
        
        # Check columns
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != mat[i][cols - 1 - j]:
                    return False
        
        return True
    
    def can_fill(row, col):
        return row >= 0 and row < n and col >= 0 and col < n and matrix[row][col] == 0
    
    def solve_recursive(row, col):
        if row >= (n + 1) // 2:
            return is_palindromic(matrix)
        
        if col >= (n + 1) // 2:
            return solve_recursive(row + 1, 0)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                
                def fill_cells(r, c, val):
                    matrix[r][c] = val
                    if r != n - 1 - r:
                        matrix[n - 1 - r][c] = val
                    if c != n - 1 - c:
                        matrix[r][n - 1 - c] = val
                    if r != n - 1 - r and c != n - 1 - c:
                        matrix[n - 1 - r][n - 1 - c] = val
                
                def get_num_filled_cells(r, c):
                    count = 1
                    if r != n - 1 - r:
                        count += 1
                    if c != n - 1 - c:
                        count += 1
                    if r != n - 1 - r and c != n - 1 - c:
                        count += 1
                    return count
                    
                
                num_filled_cells = get_num_filled_cells(row, col)
                
                if counts[num] >= num_filled_cells:
                    
                    counts[num] -= num_filled_cells
                    fill_cells(row, col, num)
                    
                    if solve_recursive(row, col + 1):
                        return True
                    
                    counts[num] += num_filled_cells
                    fill_cells(row, col, 0)
        
        return False
    
    if solve_recursive(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()