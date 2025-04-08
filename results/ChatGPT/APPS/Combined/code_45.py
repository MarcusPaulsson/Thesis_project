def find_sequence(n, k):
    # Calculate the minimum sum required for k positive integers
    min_required_sum = k * (k + 1) // 2
    
    # Check if it's possible to create such a sequence
    if min_required_sum > n:
        return -1  # Not enough sum to create a sequence of k positive integers
    
    # Calculate the remaining sum after taking the minimum required sum
    remaining = n - min_required_sum
    
    # Calculate the maximum GCD we can achieve
    g = remaining // k
    
    # Construct the sequence with the maximum GCD
    sequence = [(i + g) for i in range(1, k + 1)]
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Output the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))