def create_symmetric_matrix(n, k):
    # Check if it's possible to place k ones in a symmetric matrix
    if k > n * n or (n % 2 == 0 and k % 2 != 0):
        return -1
    
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix to make it lexicographically maximal
    for i in range(n):
        if k <= 0:
            break
        
        # Fill the diagonal first if there are remaining ones
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        # Fill the symmetric pairs (i, j) and (j, i)
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            
            if k <= 0:
                break
    
    # Return the matrix or -1 if not possible
    return matrix if k == 0 else -1

# Input reading
n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

# Output the result
if result == -1:
    print(-1)
else:
    for row in result:
        print(" ".join(map(str, row)))