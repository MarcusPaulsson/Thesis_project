def restore_permutation(n, q):
    # Initialize the permutation array with the first element as 1
    p = [0] * n
    p[0] = 1  # We can start with p[1] = 1
    
    # Calculate the rest of the permutation using q
    for i in range(1, n):
        p[i] = p[i - 1] + q[i - 1]
    
    # Find the minimum and maximum values in the permutation
    min_p = min(p)
    max_p = max(p)
    
    # Check if the permutation is valid
    if max_p - min_p + 1 != n:
        print(-1)
        return
    
    # Create a set of numbers from 1 to n
    expected_set = set(range(1, n + 1))
    # Create a set of the current permutation
    current_set = set(p)
    
    # Check if they match
    if expected_set != current_set:
        print(-1)
    else:
        print(" ".join(map(str, p)))

# Example usage:
n = int(input().strip())
q = list(map(int, input().strip().split()))
restore_permutation(n, q)