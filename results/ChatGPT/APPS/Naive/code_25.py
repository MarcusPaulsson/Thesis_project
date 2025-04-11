def create_symmetric_matrix(n, k):
    # Check if k is valid for a symmetric matrix
    if k > n * (n + 1) // 2:
        return -1
    
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix to make it lexicographically maximal
    for i in range(n):
        for j in range(i, n):
            if k > 0:
                if i == j:  # Diagonal element
                    matrix[i][j] = 1
                    k -= 1
                elif k >= 2:  # Symmetric pair
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2
    
    # If there are still ones left to place, return -1
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