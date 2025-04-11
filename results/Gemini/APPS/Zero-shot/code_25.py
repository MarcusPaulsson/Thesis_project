def solve():
    n, k = map(int, input().split())
    
    if k > n * n:
        print("-1")
        return
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k == 0:
            break
        if matrix[i][i] == 0 and k > 0:
            matrix[i][i] = 1
            k -= 1
            
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            else:
                break
        
    if k > 0:
        print("-1")
        return
    
    for row in matrix:
        print(*row)

solve()