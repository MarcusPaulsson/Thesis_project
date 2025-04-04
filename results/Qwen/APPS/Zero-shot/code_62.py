def min_operations(a, b, c):
    res = float('inf')
    A = B = C = 0
    for i in range(a, b+1):
        for j in range(i, c+1):
            if j % i == 0:
                for k in range(j, c+1):
                    if k % j == 0:
                        operations = (i-a) + (j-b) + (c-k)
                        if operations < res:
                            res = operations
                            A, B, C = i, j, k
    return res, A, B, C

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    res, A, B, C = min_operations(a, b, c)
    print(res)
    print(A, B, C)