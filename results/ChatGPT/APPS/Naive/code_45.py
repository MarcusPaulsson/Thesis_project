def find_sequence(n, k):
    # Minimum sum required for k distinct positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1  # Not enough to form k distinct positive integers
    
    # Calculate the maximum GCD that can be used
    g = (n - min_sum) // k + 1
    
    # Generate the sequence
    sequence = [(i + g) for i in range(1, k + 1)]
    
    return sequence

# Input reading
n, k = map(int, input().strip().split())

# Finding the sequence
result = find_sequence(n, k)

# Output the result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))