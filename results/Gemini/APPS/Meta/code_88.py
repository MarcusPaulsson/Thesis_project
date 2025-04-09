def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def check():
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n-1-i][j] or matrix[i][j] != matrix[i][n-1-j]:
                    return False
        return True
    
    def backtrack(row, col):
        if row == n:
            if check():
                print("YES")
                for r in matrix:
                    print(*r)
                return True
            else:
                return False
        
        if col == n:
            return backtrack(row + 1, 0)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                matrix[row][col] = num
                counts[num] -= 1
                
                if backtrack(row, col + 1):
                    return True
                
                matrix[row][col] = 0
                counts[num] += 1
        
        return False
    
    if not backtrack(0, 0):
        print("NO")

solve()