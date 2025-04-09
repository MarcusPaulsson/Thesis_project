def create_symmetric_matrix(n, k):
    # Check for impossible cases
    if k > n * n or (k % 2 == 1 and n % 2 == 1 and k > n * (n // 2 + 1)):
        return -1

    # Initialize an n x n matrix filled with zeros
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix to make it symmetric and lexicographically maximal
    for i in range(n):
        if k <= 0:
            break
        
        # Fill the diagonal
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        # Fill the symmetric pairs
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            
            if k <= 0:
                break

    # If there are leftover ones that couldn't be placed, return -1
    return -1 if k > 0 else matrix

# Read input
n, k = map(int, input().split())

# Get the symmetric matrix
result = create_symmetric_matrix(n, k)

# Output the result
if result == -1:
    print(result)
else:
    for row in result:
        print(' '.join(map(str, row)))