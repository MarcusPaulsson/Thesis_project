def create_symmetric_matrix(n, k):
    if k > n * (n + 1) // 2:
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        for j in range(i, n):
            if k >= 2 and i != j:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2
            elif k == 1 and i == j:
                matrix[i][j] = 1
                k -= 1
                break

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