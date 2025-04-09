def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # Start from an arbitrary point

    # Calculate p based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Shift p to make sure all values are positive and within the range [1, n]
    min_p = min(p)
    shift = 1 - min_p

    for i in range(n):
        p[i] += shift

    # Check if p is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Read input
n = int(input())
q = list(map(int, input().split()))

# Restore the permutation
restore_permutation(n, q)