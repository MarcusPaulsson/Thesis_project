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
                if matrix[i][j] == 0:
                    return False
        return True
    
    def is_palindromic():
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n-1-i][j] or matrix[i][j] != matrix[i][n-1-j]:
                    return False
        return True

    def backtrack(row, col):
        if row == n:
            if is_palindromic():
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
                
                r1, c1 = row, col
                r2, c2 = n - 1 - row, col
                r3, c3 = row, n - 1 - col
                r4, c4 = n - 1 - row, n - 1 - col
                
                if r1 == r2 and c1 == c3:
                    if counts[num] >= 1:
                        matrix[r1][c1] = num
                        counts[num] -= 1
                        if backtrack(row, col + 1):
                            return True
                        matrix[r1][c1] = 0
                        counts[num] += 1
                elif r1 == r2:
                    if counts[num] >= 2:
                        matrix[r1][c1] = num
                        matrix[r3][c3] = num
                        counts[num] -= 2
                        if backtrack(row, col + 1):
                            return True
                        matrix[r1][c1] = 0
                        matrix[r3][c3] = 0
                        counts[num] += 2
                elif c1 == c3:
                    if counts[num] >= 2:
                        matrix[r1][c1] = num
                        matrix[r2][c2] = num
                        counts[num] -= 2
                        if backtrack(row, col + 1):
                            return True
                        matrix[r1][c1] = 0
                        matrix[r2][c2] = 0
                        counts[num] += 2
                elif r1 == r4 and c1 == c4:
                    if counts[num] >= 4 and row != n // 2 or col != n // 2:
                        matrix[r1][c1] = num
                        matrix[r2][c2] = num
                        matrix[r3][c3] = num
                        matrix[r4][c4] = num
                        counts[num] -= 4
                        if backtrack(row, col + 1):
                            return True
                        matrix[r1][c1] = 0
                        matrix[r2][c2] = 0
                        matrix[r3][c3] = 0
                        matrix[r4][c4] = 0
                        counts[num] += 4
                else:
                    if counts[num] >= 4:
                        matrix[r1][c1] = num
                        matrix[r2][c2] = num
                        matrix[r3][c3] = num
                        matrix[r4][c4] = num
                        counts[num] -= 4
                        if backtrack(row, col + 1):
                            return True
                        matrix[r1][c1] = 0
                        matrix[r2][c2] = 0
                        matrix[r3][c3] = 0
                        matrix[r4][c4] = 0
                        counts[num] += 4
        return False

    if not backtrack(0, 0):
        print("NO")

solve()