def restore_permutation(n, q):
    # Step 1: Initialize the permutation array
    p = [0] * n
    
    # Step 2: Calculate the values of p based on q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Step 3: Normalize the permutation to start from 1
    min_value = min(p)
    offset = 1 - min_value
    
    # Step 4: Adjust the permutation values
    p = [x + offset for x in p]
    
    # Step 5: Check if the adjusted permutation is valid
    if len(set(p)) == n and all(1 <= x <= n for x in p):
        print(" ".join(map(str, p)))
    else:
        print(-1)

# Example usage:
n = int(input())
q = list(map(int, input().split()))
restore_permutation(n, q)