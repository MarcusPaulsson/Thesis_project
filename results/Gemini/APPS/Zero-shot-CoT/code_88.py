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
    
    def can_fill(row, col):
        if row >= n:
            return is_palindromic(matrix)
        
        if col >= n:
            return can_fill(row + 1, 0)
        
        if matrix[row][col] != 0:
            return can_fill(row, col + 1)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                counts[num] -= 1
                matrix[row][col] = num
                
                if row != n - 1 - row and col != n - 1 - col:
                    if counts[num] > 0:
                        counts[num] -= 1
                        matrix[n-1-row][col] = num
                        if counts[num] > 0:
                            counts[num] -= 1
                            matrix[row][n-1-col] = num
                            if counts[num] > 0:
                                counts[num] -= 1
                                matrix[n-1-row][n-1-col] = num
                                if can_fill(row, col + 1):
                                    return True
                                counts[num] += 1
                                matrix[n-1-row][n-1-col] = 0
                            else:
                                matrix[n-1-row][n-1-col] = 0
                        else:
                            matrix[row][n-1-col] = 0
                            matrix[n-1-row][n-1-col] = 0
                    else:
                        matrix[n-1-row][col] = 0
                        matrix[row][n-1-col] = 0
                        matrix[n-1-row][n-1-col] = 0
                elif row == n - 1 - row and col != n - 1 - col:
                    if counts[num] > 0:
                        counts[num] -= 1
                        matrix[row][n-1-col] = num
                        if can_fill(row, col + 1):
                            return True
                        counts[num] += 1
                        matrix[row][n-1-col] = 0
                elif row != n - 1 - row and col == n - 1 - col:
                    if counts[num] > 0:
                        counts[num] -= 1
                        matrix[n-1-row][col] = num
                        if can_fill(row, col + 1):
                            return True
                        counts[num] += 1
                        matrix[n-1-row][col] = 0
                else:
                    if can_fill(row, col + 1):
                        return True
                
                counts[num] += 1
                matrix[row][col] = 0
        
        return False
    
    if can_fill(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()