def restore_permutation(n, q):
    p = [0] * n
    p[0] = 0  # Start with an arbitrary value for p[1]
    
    # Calculate the prefix sums to find p
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Normalize the permutation to start from 1
    min_p = min(p)
    for i in range(n):
        p[i] -= min_p - 1  # Shift to make the smallest element 1
    
    # Check if p is a valid permutation
    if sorted(p) == list(range(1, n + 1)):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Example usage:
n = int(input())
q = list(map(int, input().split()))
restore_permutation(n, q)