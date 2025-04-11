def restore_permutation(n, q):
    # Initialize the permutation array
    p = [0] * n
    
    # Start with an arbitrary value for p[0]
    p[0] = 1  # We can start with any value, but 1 is a good choice
    
    # Calculate the rest of the permutation using the differences in q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Find the minimum value in p to adjust the permutation to start from 1
    min_p = min(p)
    
    # Adjust the permutation to ensure it starts from 1
    adjustment = 1 - min_p
    for i in range(n):
        p[i] += adjustment
    
    # Check if the adjusted permutation is valid
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(' '.join(map(str, p)))
    else:
        print(-1)

# Example usage
n = int(input())
q = list(map(int, input().split()))
restore_permutation(n, q)