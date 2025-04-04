def fill_matrix(n, k):
    if k > 2 * (n * (n + 1) // 2):  # Maximum number of 1's in a symmetric matrix
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        # Place 1 on the diagonal
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            
            if k <= 0:
                break
    
    if k > 0:  # If there are still ones left to place
        return -1
    
    return matrix

# Reading input
n, k = map(int, input().split())
result = fill_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(" ".join(map(str, row)))