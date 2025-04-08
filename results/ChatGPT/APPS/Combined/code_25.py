def generate_symmetric_matrix(n, k):
    if k > n * n or k < 0 or (n % 2 == 1 and k % 2 == 1):
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        for j in range(i, n):
            if i == j:  # Fill the main diagonal
                if k >= 1:
                    matrix[i][j] = 1
                    k -= 1
            else:  # Fill the symmetric pair (i, j) and (j, i)
                if k >= 2:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2

    return matrix if k == 0 else -1

# Read input
n, k = map(int, input().strip().split())
result = generate_symmetric_matrix(n, k)

# Print output
if result == -1:
    print(result)
else:
    for row in result:
        print(" ".join(map(str, row)))