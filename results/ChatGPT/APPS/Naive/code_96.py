def restore_permutation(n, q):
    # Initialize the permutation array
    p = [0] * n
    
    # Start with p[0] as an arbitrary value
    p[0] = 0
    
    # Calculate the values of p based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Normalize the permutation to start from 1
    min_value = min(p)
    for i in range(n):
        p[i] -= min_value - 1
    
    # Check if the resulting array is a valid permutation
    if sorted(p) == list(range(1, n + 1)):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Example usage:
n = int(input())
q = list(map(int, input().split()))
restore_permutation(n, q)