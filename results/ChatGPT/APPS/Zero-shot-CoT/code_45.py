def find_sequence(n, k):
    # Minimum sum of first k natural numbers is k * (k + 1) / 2
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1  # Not enough to create the sequence
    
    # The greatest common divisor can be at most n // k
    gcd = (n - min_sum) // k + 1  # This is the maximum we can use for gcd
    
    # Calculate the base sequence
    base_sequence = [i for i in range(1, k + 1)]
    
    # Calculate the adjustment needed
    adjustment = gcd * k
    
    # Final sequence
    result_sequence = [x + adjustment for x in base_sequence]
    
    # Check if the sum is equal to n
    if sum(result_sequence) == n:
        return result_sequence
    else:
        return -1

# Read input
n, k = map(int, input().split())

# Get the result
result = find_sequence(n, k)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))