def restore_permutation(n, q):
    # Initialize p with the first element
    p = [0] * n
    p[0] = 0  # We will adjust this later

    # Calculate p based on the differences in q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Find the minimum value in p to normalize the values
    min_p = min(p)

    # Normalize p so that the smallest value becomes 1
    for i in range(n):
        p[i] -= min_p - 1

    # Check if p is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Read input
n = int(input())
q = list(map(int, input().split()))

# Restore the permutation
restore_permutation(n, q)