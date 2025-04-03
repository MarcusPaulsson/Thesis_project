def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # We will adjust this later
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Finding the minimum value to shift the permutation to start from 1
    min_p = min(p)
    shift = 1 - min_p

    # Adjusting the permutation
    for i in range(n):
        p[i] += shift

    # Check if the result is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Read input
n = int(input())
q = list(map(int, input().split()))

restore_permutation(n, q)