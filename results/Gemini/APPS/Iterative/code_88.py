def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def find_solution():
        
        def is_valid():
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] != matrix[n-1-i][j] or matrix[i][j] != matrix[i][n-1-j]:
                        return False
            return True

        def solve_recursive(row, col):
            if row == (n + 1) // 2:
                return is_valid()
            
            if col == (n + 1) // 2:
                return solve_recursive(row + 1, 0)
            
            for val in sorted(list(counts.keys())):
                if counts[val] > 0:
                    
                    need = 1
                    if row != n - 1 - row:
                        need += 1
                    if col != n - 1 - col:
                        need += 1
                    if row != n - 1 - row and col != n - 1 - col:
                        need += 1
                    
                    if counts[val] >= need:
                        
                        matrix[row][col] = val
                        matrix[n-1-row][col] = val
                        matrix[row][n-1-col] = val
                        matrix[n-1-row][n-1-col] = val
                        
                        counts[val] -= need

                        if solve_recursive(row, col + 1):
                            return True

                        counts[val] += need
                        matrix[row][col] = 0
                        matrix[n-1-row][col] = 0
                        matrix[row][n-1-col] = 0
                        matrix[n-1-row][n-1-col] = 0
            return False

        return solve_recursive(0, 0)

    if find_solution():
        print("YES")
        for row in matrix:
            print(*row)
    else:
        print("NO")

solve()