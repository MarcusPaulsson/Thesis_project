def create_symmetric_matrix(n, k):
    # Check for impossible cases
    if k > n * n or (n % 2 == 0 and k % 2 != 0) or (n % 2 == 1 and k > n * n - (n // 2)):
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix
    for i in range(n):
        if k <= 0:
            break
        # Place a 1 in the diagonal
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        # Fill the symmetric pairs
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2

    # If we still have ones left, it means we couldn't place them appropriately
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