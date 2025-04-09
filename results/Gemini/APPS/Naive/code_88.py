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
                counts[num] -= 1
                matrix[row][col] = num
                
                row_sym = n - 1 - row
                col_sym = n - 1 - col
                
                matrix[row_sym][col] = num
                matrix[row][col_sym] = num
                matrix[row_sym][col_sym] = num
                
                if backtrack(row, col + 1):
                    return True
                
                counts[num] += 1
                matrix[row][col] = 0
                matrix[row_sym][col] = 0
                matrix[row][col_sym] = 0
                matrix[row_sym][col_sym] = 0
        
        return False

    
    if backtrack(0, 0):
        return
    else:
        print("NO")

solve()