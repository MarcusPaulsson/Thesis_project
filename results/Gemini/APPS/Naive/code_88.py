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
                
                
                r_sym = n - 1 - row
                c_sym = n - 1 - col
                
                if row == r_sym and col == c_sym:
                    if counts[num] >= 1:
                        matrix[row][col] = num
                        counts[num] -= 1
                        if backtrack(row, col + 1):
                            return True
                        matrix[row][col] = 0
                        counts[num] += 1
                elif row == r_sym:
                    if counts[num] >= 2:
                        matrix[row][col] = num
                        matrix[row][c_sym] = num
                        counts[num] -= 2
                        if backtrack(row, col + 1):
                            return True
                        matrix[row][col] = 0
                        matrix[row][c_sym] = 0
                        counts[num] += 2
                elif col == c_sym:
                    if counts[num] >= 2:
                        matrix[row][col] = num
                        matrix[r_sym][col] = num
                        counts[num] -= 2
                        if backtrack(row, col + 1):
                            return True
                        matrix[row][col] = 0
                        matrix[r_sym][col] = 0
                        counts[num] += 2
                else:
                    if counts[num] >= 4:
                        matrix[row][col] = num
                        matrix[row][c_sym] = num
                        matrix[r_sym][col] = num
                        matrix[r_sym][c_sym] = num
                        counts[num] -= 4
                        if backtrack(row, col + 1):
                            return True
                        matrix[row][col] = 0
                        matrix[row][c_sym] = 0
                        matrix[r_sym][col] = 0
                        matrix[r_sym][c_sym] = 0
                        counts[num] += 4
        
        return False

    if backtrack(0, 0):
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()