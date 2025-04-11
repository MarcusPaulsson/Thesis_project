def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def is_palindromic(mat):
        for i in range(n):
            for j in range(n):
                if mat[i][j] != mat[n-1-i][j] or mat[i][j] != mat[i][n-1-j]:
                    return False
        return True

    def backtrack(row, col):
        if row == n:
            if is_palindromic(matrix):
                print("YES")
                for r in matrix:
                    print(*r)
                return True
            else:
                return False
        
        next_row = row
        next_col = col + 1
        if next_col == n:
            next_row += 1
            next_col = 0
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                matrix[row][col] = num
                counts[num] -= 1
                
                if row == n - 1 - row and col == n - 1 - col:
                    if backtrack(next_row, next_col):
                        return True
                elif row == n - 1 - row:
                    if counts.get(num,0) >= 1:
                        matrix[row][n-1-col] = num
                        counts[num] -= 1
                        if backtrack(next_row, next_col):
                            return True
                        counts[num] += 1
                        matrix[row][n-1-col] = 0
                elif col == n - 1 - col:
                    if counts.get(num,0) >= 1:
                        matrix[n-1-row][col] = num
                        counts[num] -= 1
                        if backtrack(next_row, next_col):
                            return True
                        counts[num] += 1
                        matrix[n-1-row][col] = 0
                else:
                    if counts.get(num,0) >= 3:
                        matrix[n-1-row][col] = num
                        matrix[row][n-1-col] = num
                        matrix[n-1-row][n-1-col] = num
                        counts[num] -= 3
                        if backtrack(next_row, next_col):
                            return True
                        counts[num] += 3
                        matrix[n-1-row][col] = 0
                        matrix[row][n-1-col] = 0
                        matrix[n-1-row][n-1-col] = 0
                
                counts[num] += 1
                matrix[row][col] = 0
        
        return False
    
    if not backtrack(0, 0):
        print("NO")

solve()