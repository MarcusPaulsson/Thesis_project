def find_sequence(n, k):
    # Minimum sum of first k positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # Start with the first k positive integers multiplied by max_gcd
    sequence = [i * max_gcd for i in range(1, k + 1)]
    
    # Calculate the current sum of the sequence
    current_sum = sum(sequence)
    
    # Adjust the last element to match the required sum n
    sequence[-1] += n - current_sum
    
    # Check if the last element is still greater than the previous one
    if sequence[-1] <= sequence[-2]:
        return -1
    
    return sequence

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

# Output result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))