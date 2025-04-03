def create_symmetric_matrix(n, k):
    if k > n * n or k % 2 != 0 and k > n * n - n:
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k >= 2:
            matrix[i][i] = 1
            k -= 1
            if k > 0 and i + 1 < n:
                matrix[i][i + 1] = 1
                matrix[i + 1][i] = 1
                k -= 2

    if k > 0:
        return -1
    
    return matrix

n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))