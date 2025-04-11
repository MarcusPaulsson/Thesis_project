def create_symmetric_matrix(n, k):
    if k > n * n or (k % 2 != 0 and n % 2 == 0):
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k >= 2 and i != n - 1 - i:
            matrix[i][i] = 1
            matrix[n - 1 - i][n - 1 - i] = 1
            k -= 2
        elif k >= 1 and i == n - 1 - i:
            matrix[i][i] = 1
            k -= 1
            
        if k == 0:
            break
    
    if k > 0:
        return -1
    
    return matrix

n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))