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
            return is_palindromic(matrix)
        
        if col == n:
            return backtrack(row + 1, 0)
        
        if matrix[row][col] != 0:
            return backtrack(row, col + 1)
        
        for num in list(counts.keys()):
            if counts[num] > 0:
                
                required = 1
                
                r1, c1 = row, col
                r2, c2 = n - 1 - row, col
                r3, c3 = row, n - 1 - col
                r4, c4 = n - 1 - row, n - 1 - col
                
                coords = [(r1, c1)]
                if r1 != r2 or c1 != c2:
                    coords.append((r2, c2))
                    required += 1
                if (r1 != r3 or c1 != c3) and (r2 != r3 or c2 != c3):
                    coords.append((r3, c3))
                    required += 1
                if (r1 != r4 or c1 != c4) and (r2 != r4 or c2 != c4) and (r3 != r4 or c3 != c4):
                    coords.append((r4, c4))
                    required += 1
                
                if counts[num] >= required:
                    counts[num] -= required
                    for r, c in coords:
                        matrix[r][c] = num

                    if backtrack(row, col + 1):
                        return True
                    
                    counts[num] += required
                    for r, c in coords:
                        matrix[r][c] = 0
        
        return False

    if backtrack(0, 0):
        print("YES")
        for r in matrix:
            print(*r)
    else:
        print("NO")

solve()