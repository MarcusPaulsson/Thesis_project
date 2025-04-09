def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def check(matrix):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n-1-i][j] or matrix[i][j] != matrix[i][n-1-j]:
                    return False
        return True
    
    def backtrack(row, col):
        if row == n:
            return check(matrix)
        
        if col == n:
            return backtrack(row + 1, 0)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                matrix[row][col] = num
                counts[num] -= 1
                
                if backtrack(row, col + 1):
                    return True
                
                counts[num] += 1
                matrix[row][col] = 0
                
        return False

    def fill_matrix():
        for i in range((n + 1) // 2):
            for j in range((n + 1) // 2):
                if matrix[i][j] == 0:
                  
                    found = False
                    for num in list(counts.keys()):
                        
                        needed = 1
                        if i != n - 1 - i:
                            needed += 1
                        if j != n - 1 - j:
                            needed += 1
                        if i != n - 1 - i and j != n - 1 - j:
                            needed += 1
                            
                        if counts[num] >= needed:
                            matrix[i][j] = num
                            counts[num] -= 1
                            
                            if i != n - 1 - i:
                                matrix[n-1-i][j] = num
                                counts[num] -= 1
                            
                            if j != n - 1 - j:
                                matrix[i][n-1-j] = num
                                counts[num] -= 1
                            
                            if i != n - 1 - i and j != n - 1 - j:
                                matrix[n-1-i][n-1-j] = num
                                counts[num] -= 1
                            
                            found = True
                            break
                    
                    if not found:
                        return False
        return True
    
    if fill_matrix():
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()