def create_matrix(n, k):
    # Calculate the maximum number of ones we can place
    max_ones = n * (n + 1) // 2
    
    if k > max_ones:
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k > 0:
            # Place 1s in the diagonal first
            if k > 0:
                matrix[i][i] = 1
                k -= 1
            
            # Then try to fill the upper triangle
            for j in range(i + 1, n):
                if k >= 2:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    k -= 2
                
    return matrix if k == 0 else -1

# Reading input
n, k = map(int, input().split())
result = create_matrix(n, k)

# Output the result
if result == -1:
    print(result)
else:
    for row in result:
        print(' '.join(map(str, row)))