def find_sequence(n, k):
    # Calculate the minimum sum of the first k positive integers
    min_sum = k * (k + 1) // 2
    
    # If n is less than the minimum sum, return -1
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # Calculate the actual sequence
    sequence = [(i + 1) for i in range(k)]
    
    # Calculate the current sum of the sequence
    current_sum = sum(sequence)
    
    # Adjust the last element to make the sum equal to n
    sequence[-1] += (n - current_sum)
    
    # Scale the sequence by the maximum GCD
    sequence = [x * max_gcd for x in sequence]
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print the result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))