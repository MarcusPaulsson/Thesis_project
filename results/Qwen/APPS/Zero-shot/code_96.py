def restore_permutation(n, q):
    p = [0] * n
    p[0] = 1
    for i in range(1, n):
        p[i] = p[i-1] + q[i-1]
        if p[i] < 1 or p[i] > n or p[i] in p[:i]:
            return -1
    return p

n = int(input())
q = list(map(int, input().split()))
p = restore_permutation(n, q)
if p == -1:
    print(-1)
else:
    print(*p)