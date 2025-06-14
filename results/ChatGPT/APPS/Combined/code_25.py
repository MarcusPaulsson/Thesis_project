def create_symmetric_matrix(n, k):
    max_possible_ones = n * (n + 1) // 2
    if k > max_possible_ones:
        return -1

    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        if k <= 0:
            break
        # Fill the diagonal first
        if k > 0:
            matrix[i][i] = 1
            k -= 1
        
        for j in range(i + 1, n):
            if k <= 1:
                break
            # Fill the symmetric positions
            if k >= 2:
                matrix[i][j] = 1
                matrix[j][i] = 1
                k -= 2

    return matrix if k == 0 else -1

n, k = map(int, input().split())
result = create_symmetric_matrix(n, k)

if result == -1:
    print(-1)
else:
    for row in result:
        print(' '.join(map(str, row)))