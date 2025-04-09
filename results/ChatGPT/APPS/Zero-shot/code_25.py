def create_symmetrical_matrix(n, k):
    # Maximum number of 1's we can place in a symmetric matrix
    max_ones = n * (n + 1) // 2
    if k > max_ones:
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k == 0:
            break
        # Fill the diagonal first
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        # Then fill the upper triangle
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            if k == 0:
                break
    
    # Check if we have used exactly k ones
    if k > 0:
        return -1
    
    return matrix

# Read input
n, k = map(int, input().split())
result = create_symmetrical_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))