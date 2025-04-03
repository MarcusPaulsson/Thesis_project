def create_matrix(n, k):
    if k > n * n or k < 0:
        return -1
    if k % 2 == 1 and n % 2 == 0:
        return -1
    
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix to make it lexicographically maximal
    for i in range(n):
        for j in range(i, n):
            if k >= 2 and i != j:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            elif k >= 1 and i == j:
                matrix[i][j] = 1
                k -= 1
            if k == 0:
                break
        if k == 0:
            break
    
    # If there are still ones left, return -1
    if k > 0:
        return -1
    
    return matrix

n, k = map(int, input().split())
result = create_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))