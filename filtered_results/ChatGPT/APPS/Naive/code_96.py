def restore_permutation(n, q):
    # Initialize the permutation array
    p = [0] * n
    
    # Set the first element
    p[0] = 0
    
    # Calculate the prefix sums to find the permutation values
    for i in range(1, n):
        p[i] = p[i-1] + q[i-1]
    
    # Find the minimum value in p to adjust to make it a valid permutation
    min_p = min(p)
    
    # Adjust the permutation to start from 1
    adjustment = 1 - min_p
    for i in range(n):
        p[i] += adjustment
    
    # Check if the adjusted permutation is valid
    if len(set(p)) != n or any(x < 1 or x > n for x in p):
        print(-1)
    else:
        print(" ".join(map(str, p)))

# Read input
n = int(input())
q = list(map(int, input().split()))

# Restore and print the permutation
restore_permutation(n, q)