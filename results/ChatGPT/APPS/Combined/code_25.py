def create_symmetric_matrix(n, k):
    # Validate input k
    if k > n * n or k < 0 or (n % 2 == 0 and k % 2 != 0):
        return -1

    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix to make it lexicographically maximal
    for i in range(n):
        if k <= 0:
            break
        
        # Fill the diagonal
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        # Fill symmetric pairs
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            if k <= 0:
                break

    # Check if there are remaining ones that couldn't be placed
    return -1 if k > 0 else matrix

# Read input
n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

# Print output
if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))