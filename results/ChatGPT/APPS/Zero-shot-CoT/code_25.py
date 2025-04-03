def create_matrix(n, k):
    if k > n * n or k % 2 != 0 and n % 2 == 0:
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the diagonal first
    for i in range(n):
        if k > 0:
            matrix[i][i] = 1
            k -= 1
            
    # Fill the upper triangle (excluding the diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            if k <= 0:
                break
    
    # If we still have k ones left, it's impossible
    if k > 0:
        return -1
    
    return matrix

# Input reading
n, k = map(int, input().split())
result = create_matrix(n, k)

# Output the result
if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))