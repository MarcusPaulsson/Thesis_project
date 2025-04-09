def find_sequence(n, k):
    # Minimum sum required for the first k positive integers
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        return -1
    
    # Calculate the maximum gcd
    gcd = (n - min_sum) // k + 1
    # Create the sequence
    sequence = [(i + gcd) for i in range(1, k + 1)]
    
    # If the sum of the sequence is less than n, we need to adjust the last element
    current_sum = sum(sequence)
    if current_sum < n:
        sequence[-1] += n - current_sum
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))