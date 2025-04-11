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
    
    def can_fill(row, col):
        if row >= (n + 1) // 2:
            return True
        
        if col >= (n + 1) // 2:
            return can_fill(row + 1, 0)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                counts[num] -= 1
                matrix[row][col] = num
                matrix[n-1-row][col] = num
                matrix[row][n-1-col] = num
                matrix[n-1-row][n-1-col] = num
                
                if can_fill(row, col + 1):
                    return True
                
                counts[num] += 1
                matrix[row][col] = 0
                matrix[n-1-row][col] = 0
                matrix[row][n-1-col] = 0
                matrix[n-1-row][n-1-col] = 0
        
        return False
    
    if can_fill(0, 0):
        if is_valid(matrix) and is_palindromic(matrix):
            print("YES")
            for row in matrix:
                print(*row)
        else:
            print("NO")
    else:
        print("NO")

solve()