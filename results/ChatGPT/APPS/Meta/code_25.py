def create_symmetric_matrix(n, k):
    if k > n * (n + 1) // 2:
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        for j in range(i, n):
            if k <= 0:
                break
            if i == j:  # diagonal element
                if k >= 1:
                    matrix[i][j] = 1
                    k -= 1
            else:  # symmetric pair
                if k >= 2:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2
    
    return matrix if k == 0 else -1

# Read input
n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

# Output result
if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))