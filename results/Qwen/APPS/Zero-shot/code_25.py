def lexicographically_maximal_symmetric_matrix(n, k):
    if k > n * n // 2:
        return -1

    matrix = [[0] * n for _ in range(n)]
    ones = k

    for i in range(n):
        for j in range(i, n):
            if ones > 0:
                matrix[i][j] = 1
                matrix[j][i] = 1
                ones -= 1
            else:
                break
        if ones == 0:
            break

    return matrix

n, k = map(int, input().split())
result = lexicographically_maximal_symmetric_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))