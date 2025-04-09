def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # We will adjust later

    # Calculate the prefix sums based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Find the minimum value in p to adjust the permutation to start from 1
    min_p = min(p)

    # Adjust all values to make them start from 1
    for i in range(n):
        p[i] -= min_p - 1

    # Check if we have a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Reading input
n = int(input().strip())
q = list(map(int, input().strip().split()))

# Restore the permutation
restore_permutation(n, q)