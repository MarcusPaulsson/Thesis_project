def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # We can start from any arbitrary value, we will adjust later

    # Calculate the prefix sums to find the values of p
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Find the minimum value in p to adjust the permutation to start from 1
    min_p = min(p)
    adjustment = 1 - min_p

    # Adjust the permutation
    for i in range(n):
        p[i] += adjustment

    # Check if the adjusted permutation is valid
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Read input
n = int(input())
q = list(map(int, input().split()))

# Restore the permutation
restore_permutation(n, q)