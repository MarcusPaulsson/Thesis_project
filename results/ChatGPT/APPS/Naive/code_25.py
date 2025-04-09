def create_symmetric_matrix(n, k):
    # Check if it's possible to place k ones
    max_ones = n * (n + 1) // 2
    if k > max_ones:
        return -1

    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix symmetrically and lexicographically maximal
    for i in range(n):
        if k <= 0:
            break
        for j in range(i, n):
            if k > 0:
                matrix[i][j] = 1
                if i != j:
                    matrix[j][i] = 1
                k -= 2 if i != j else 1

    return matrix

# Input reading
n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

# Output result
if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))