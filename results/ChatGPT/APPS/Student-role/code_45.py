def find_sequence(n, k):
    # Minimum sum of first k positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use
    max_gcd = (n - min_sum) // k + 1
    
    # Create the sequence
    sequence = [(i + max_gcd) for i in range(1, k + 1)]
    
    return sequence

# Read input
n, k = map(int, input().split())

# Get the result
result = find_sequence(n, k)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))