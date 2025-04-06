def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # Starting from an arbitrary point (0)
    
    # Calculate p from q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Adjust to make the minimum value in p to be 1
    min_p = min(p)
    if min_p < 1:
        # Shift all values up to make the smallest value 1
        shift = 1 - min_p
        for i in range(n):
            p[i] += shift
    
    # Check if p is a valid permutation
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Input processing
n = int(input())
q = list(map(int, input().split()))

restore_permutation(n, q)