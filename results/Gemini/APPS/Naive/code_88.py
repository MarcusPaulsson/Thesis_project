def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def is_valid(matrix):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    return False
        return True
    
    def is_palindromic(matrix):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n-1-i][j] or matrix[i][j] != matrix[i][n-1-j]:
                    return False
        return True
    
    def backtrack(row, col):
        if row == n:
            if is_valid(matrix) and is_palindromic(matrix):
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
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                
                matrix[row][col] = num
                matrix[n-1-row][col] = num
                matrix[row][n-1-col] = num
                matrix[n-1-row][n-1-col] = num
                
                counts[num] -= 1
                if counts[num] == 0:
                    del counts[num]
                
                if backtrack(row, col + 1):
                    return True
                
                counts[num] = counts.get(num, 0) + 1
                matrix[row][col] = 0
                matrix[n-1-row][col] = 0
                matrix[row][n-1-col] = 0
                matrix[n-1-row][n-1-col] = 0
        
        return False
    
    if not backtrack(0, 0):
        print("NO")

solve()