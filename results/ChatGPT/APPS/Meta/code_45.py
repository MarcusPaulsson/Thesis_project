def find_sequence(n, k):
    # The minimum sum of the first k positive integers is k * (k + 1) // 2
    min_sum = k * (k + 1) // 2
    
    # If n is less than the minimum sum, it's impossible to form such a sequence
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    # We will try to use the largest GCD possible that allows us to form the sequence
    max_gcd = n // k
    
    # Start with the first k numbers multiplied by the GCD
    sequence = [(i + 1) * max_gcd for i in range(k)]
    
    # Calculate the current sum of this sequence
    current_sum = sum(sequence)
    
    # If the current sum is less than n, we need to adjust the last element
    if current_sum < n:
        # Increase the last element to make the sum equal to n
        sequence[-1] += (n - current_sum)
    
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