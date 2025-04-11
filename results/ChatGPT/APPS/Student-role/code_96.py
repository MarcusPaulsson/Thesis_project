def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # We can start from any arbitrary number, we'll adjust later

    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    min_p = min(p)
    # Adjust the permutation to start from 1
    offset = 1 - min_p

    for i in range(n):
        p[i] += offset

    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Read input
n = int(input())
q = list(map(int, input().split()))

restore_permutation(n, q)