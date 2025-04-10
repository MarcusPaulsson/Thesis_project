def create_symmetric_matrix(n, k):
    if k > n * n or (k % 2 != 0 and n % 2 == 0):
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        # Place 1s on the diagonal
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        # Place 1s in the upper triangle
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            
            if k <= 0:
                break

    if k > 0:
        return -1

    return matrix

# Read input
n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

# Output result
if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))