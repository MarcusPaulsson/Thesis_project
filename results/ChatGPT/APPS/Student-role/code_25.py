def create_symmetric_matrix(n, k):
    if k > n * n:
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if i == j:  # Diagonal element
                if k > 0:
                    matrix[i][j] = 1
                    k -= 1
            else:  # Off-diagonal elements
                if k >= 2:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2
            
            if k == 0:
                break
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