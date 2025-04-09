def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    
    matrix = [[0] * n for _ in range(n)]
    
    def can_place(row, col, val):
        if matrix[row][col] != 0:
            return False
        return True
    
    def fill_matrix():
        for i in range((n + 1) // 2):
            for j in range((n + 1) // 2):
                if matrix[i][j] == 0:
                    found = False
                    for val in sorted(counts.keys()):
                        if counts[val] >= 1 + (i != n - 1 - i) + (j != n - 1 - j) + (i != n - 1 - i and j != n - 1 - j):
                            matrix[i][j] = val
                            counts[val] -= 1
                            
                            matrix[n - 1 - i][j] = val
                            counts[val] -= (i != n - 1 - i)
                            
                            matrix[i][n - 1 - j] = val
                            counts[val] -= (j != n - 1 - j)
                            
                            matrix[n - 1 - i][n - 1 - j] = val
                            counts[val] -= (i != n - 1 - i and j != n - 1 - j)
                            
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