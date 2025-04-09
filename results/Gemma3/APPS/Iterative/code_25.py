def solve():
    n, k = map(int, input().split())
    
    if k > n * (n + 1) // 2:
        print(-1)
        return
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if k > 0:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 1
            else:
                break
        if k <= 0:
            break
            
    
    for i in range(n):
        print(*matrix[i])

solve()