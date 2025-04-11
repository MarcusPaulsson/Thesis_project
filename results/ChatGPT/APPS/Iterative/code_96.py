def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # Start with an arbitrary value

    # Calculate the prefix sums to find the values of p
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Normalize the permutation to start from 1
    min_value = min(p)
    for i in range(n):
        p[i] -= min_value - 1

    # Check if the resulting array is a valid permutation
    if sorted(p) == list(range(1, n + 1)):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Read input
n = int(input())
q = list(map(int, input().split()))

# Restore the permutation
restore_permutation(n, q)