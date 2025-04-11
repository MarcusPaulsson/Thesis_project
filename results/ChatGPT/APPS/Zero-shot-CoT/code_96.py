def restore_permutation(n, q):
    # Initialize the first element of the permutation
    p = [0] * n
    p[0] = 1  # Start with p1 = 1

    # Calculate the rest of the permutation based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]

    # Find the minimum and maximum values in the permutation
    min_p = min(p)
    max_p = max(p)

    # Check if the values are within the valid range and unique
    if max_p - min_p + 1 != n or len(set(p)) != n:
        print(-1)
    else:
        # Adjust the permutation to start from 1
        adjustment = 1 - min_p
        p = [x + adjustment for x in p]
        print(" ".join(map(str, p)))

# Read input
n = int(input())
q = list(map(int, input().split()))

# Restore the permutation
restore_permutation(n, q)