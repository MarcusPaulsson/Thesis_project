def find_sequence(n, k):
    # Minimum sum of the first k positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use
    max_gcd = (n - min_sum) // k + 1
    
    # Create the sequence
    sequence = [(i + max_gcd) for i in range(1, k + 1)]
    
    # Adjust the last element to ensure the sum is exactly n
    sequence[-1] += (n - sum(sequence))
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))