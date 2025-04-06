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
        
        if col == n:
            return backtrack(row + 1, 0)
        
        if matrix[row][col] != 0:
            return backtrack(row, col + 1)
        
        for val in list(counts.keys()):
            if counts[val] > 0:
                
                counts[val] -= 1
                matrix[row][col] = val
                
                
                if row != n - 1 - row and col != n - 1 - col:
                    if counts[val] > 0:
                        counts[val] -= 1
                        matrix[n-1-row][col] = val
                        
                        if counts[val] > 0:
                            counts[val] -= 1
                            matrix[row][n-1-col] = val
                            
                            if counts[val] > 0:
                                counts[val] -= 1
                                matrix[n-1-row][n-1-col] = val
                                
                                if backtrack(row, col + 1):
                                    return True
                                
                                counts[val] += 1
                                matrix[n-1-row][n-1-col] = 0
                            
                            counts[val] += 1
                            matrix[row][n-1-col] = 0
                        
                        counts[val] += 1
                        matrix[n-1-row][col] = 0
                elif row == n - 1 - row and col != n - 1 - col:
                    if counts[val] > 0:
                        counts[val] -= 1
                        matrix[row][n-1-col] = val
                        if backtrack(row, col + 1):
                            return True
                        counts[val] += 1
                        matrix[row][n-1-col] = 0
                    
                elif row != n - 1 - row and col == n - 1 - col:
                    if counts[val] > 0:
                        counts[val] -= 1
                        matrix[n-1-row][col] = val
                        if backtrack(row, col + 1):
                            return True
                        counts[val] += 1
                        matrix[n-1-row][col] = 0
                else:
                    if backtrack(row, col + 1):
                        return True
                        
                counts[val] += 1
                matrix[row][col] = 0
        
        return False

    if not backtrack(0, 0):
        print("NO")

solve()