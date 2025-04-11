def find_sequence(n, k):
    # Minimum sum of first k positive integers is k * (k + 1) // 2
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # We need to find the largest GCD that allows us to create a valid sequence
    for g in range(max_gcd, 0, -1):
        # Calculate the adjusted sum we need to reach
        adjusted_n = n // g
        
        # Check if we can form the sequence with this GCD
        if adjusted_n >= min_sum:
            # Create the sequence
            sequence = [(i + 1) * g for i in range(k)]
            return sequence
    
    return -1

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))