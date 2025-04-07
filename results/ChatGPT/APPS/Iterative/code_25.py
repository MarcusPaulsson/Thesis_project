def create_matrix(n, k):
    max_possible_k = n * (n + 1) // 2
    if k > max_possible_k:
        return -1  # Not enough space to place k ones
    
    matrix = [[0] * n for _ in range(n)]

    # Fill the matrix to be lexicographically maximal
    for i in range(n):
        if k <= 0:
            break
        for j in range(i, n):
            if k > 0:
                matrix[i][j] = 1
                if i != j:
                    matrix[j][i] = 1  # Make it symmetric
                    k -= 2  # Off-diagonal counts as two
                else:
                    k -= 1  # Diagonal counts as one

    if k > 0:
        return -1  # Still remaining ones that couldn't be placed

    return matrix

# Input reading
n, k = map(int, input().split())
result = create_matrix(n, k)

# Output result
if result == -1:
    print(result)
else:
    for row in result:
        print(" ".join(map(str, row)))