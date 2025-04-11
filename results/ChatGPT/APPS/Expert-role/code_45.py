def find_sequence(n, k):
    # Minimum sum of the first k positive integers
    min_sum = k * (k + 1) // 2
    
    # If n is less than the minimum sum, it's impossible to form the sequence
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # Start with the first k positive integers
    sequence = list(range(1, k + 1))
    
    # Calculate the current sum of the sequence
    current_sum = sum(sequence)
    
    # Calculate the difference we need to make up
    diff = n - current_sum
    
    # We can increase each element in the sequence by the same amount
    # to maintain the strictly increasing property
    # We can add `diff // k` to each element
    increment = diff // k
    
    # Add the increment to each element
    for i in range(k):
        sequence[i] += increment
    
    # Check if we have any remaining difference to distribute
    remaining = diff % k
    
    # Distribute the remaining difference
    for i in range(remaining):
        sequence[i] += 1
    
    # The GCD of the sequence will be max_gcd
    # Scale the sequence by max_gcd
    sequence = [x * max_gcd for x in sequence]
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))