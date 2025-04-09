def restore_permutation(n, q):
    # Step 1: Initialize permutation array with first element
    p = [0] * n
    p[0] = 1  # Starting with p1 = 1 (arbitrary choice)

    # Step 2: Generate the permutation based on differences in q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Step 3: Normalize the permutation to ensure it starts from 1
    min_value = min(p)
    for i in range(n):
        p[i] -= min_value - 1  # Shift to start from 1

    # Step 4: Validate if the resulting array is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Example usage
n = int(input())
q = list(map(int, input().split()))
restore_permutation(n, q)