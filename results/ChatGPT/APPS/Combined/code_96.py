def restore_permutation(n, q):
    # Initialize the permutation array
    p = [0] * n

    # Calculate the prefix sums to find the permutation
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Find the minimum value in p to adjust the permutation to start from 1
    min_p = min(p)
    offset = 1 - min_p

    # Adjust the permutation
    for i in range(n):
        p[i] += offset

    # Validate the adjusted permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)