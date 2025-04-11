def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def check_palindrome(mat):
        for i in range(n):
            for j in range(n):
                if mat[i][j] != mat[n-1-i][j] or mat[i][j] != mat[i][n-1-j]:
                    return False
        return True
    
    def backtrack(row, col):
        if row == n:
            if check_palindrome(matrix):
                print("YES")
                for r in matrix:
                    print(*r)
                return True
            else:
                return False
        
        next_row = row
        next_col = col + 1
        if next_col == n:
            next_row = row + 1
            next_col = 0
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                matrix[row][col] = num
                counts[num] -= 1
                
                if backtrack(next_row, next_col):
                    return True
                
                matrix[row][col] = 0
                counts[num] += 1
        
        return False
    
    if backtrack(0, 0):
        return
    else:
        print("NO")

solve()