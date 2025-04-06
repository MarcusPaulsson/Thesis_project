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
        return row >= 0 and row < n and col >= 0 and col < n and matrix[row][col] == 0
    
    def backtrack(row, col):
        if row >= (n + 1) // 2:
            return True
        
        if col >= (n + 1) // 2:
            return backtrack(row + 1, 0)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                counts[num] -= 1
                matrix[row][col] = num
                
                if n % 2 == 1 and row == n // 2 and col == n // 2:
                    if backtrack(row, col + 1):
                        return True
                elif n % 2 == 1 and (row == n // 2 or col == n // 2):
                    if can_fill(row, n - 1 - col):
                        if counts[num] > 0:
                            counts[num] -= 1
                            matrix[row][n - 1 - col] = num
                            if backtrack(row, col + 1):
                                return True
                            matrix[row][n - 1 - col] = 0
                            counts[num] += 1
                    
                else:
                    if can_fill(row, n - 1 - col) and can_fill(n - 1 - row, col) and can_fill(n - 1 - row, n - 1 - col):
                        if counts[num] > 0:
                            counts[num] -= 1
                            matrix[row][n - 1 - col] = num
                            matrix[n - 1 - row][col] = num
                            matrix[n - 1 - row][n - 1 - col] = num
                            if backtrack(row, col + 1):
                                return True
                            matrix[row][n - 1 - col] = 0
                            matrix[n - 1 - row][col] = 0
                            matrix[n - 1 - row][n - 1 - col] = 0
                            counts[num] += 1
                
                matrix[row][col] = 0
                counts[num] += 1
        
        return False
    
    if backtrack(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()