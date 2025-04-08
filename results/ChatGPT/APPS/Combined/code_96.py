def restore_permutation(n, q):
    # Step 1: Calculate the prefix sums to find the permutation p
    p = [0] * n
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Step 2: Normalize the permutation to start from 1
    min_p = min(p)
    offset = 1 - min_p
    
    # Apply offset to ensure all values are positive and start from 1
    p = [x + offset for x in p]

    # Step 3: Check if p is a valid permutation
    if len(set(p)) != n or any(x < 1 or x > n for x in p):
        return -1
    return p

# Read input
n = int(input())
q = list(map(int, input().split()))

# Get the result
result = restore_permutation(n, q)

# Print the output
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))