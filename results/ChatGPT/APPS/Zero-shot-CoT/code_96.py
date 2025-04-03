def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # Start with an arbitrary value
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Shift the permutation to make all values positive and in the range [1, n]
    min_value = min(p)
    shift = 1 - min_value

    for i in range(n):
        p[i] += shift

    # Check if the result is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Reading input
n = int(input())
q = list(map(int, input().split()))

# Restoring the permutation
restore_permutation(n, q)