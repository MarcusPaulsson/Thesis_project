def restore_permutation(n, q):
    # Initialize the permutation array
    p = [0] * n
    
    # Set the first element of p
    p[0] = 1  # We can start with any number, let's start with 1
    
    # Calculate the rest of the elements based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Check if the permutation is valid
    if len(set(p)) != n or any(x < 1 or x > n for x in p):
        print(-1)
    else:
        print(' '.join(map(str, p)))

# Example usage:
# n = 3
# q = [-2, 1]
# restore_permutation(n, q)