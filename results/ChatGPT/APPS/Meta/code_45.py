def find_sequence(n, k):
    # The minimum sum of the first k positive integers is k * (k + 1) // 2
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1  # Not enough to form a strictly increasing sequence of k numbers
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # We can form the sequence by using the first k integers multiplied by the max_gcd
    sequence = [(i + 1) * max_gcd for i in range(k)]
    
    # Calculate the sum of this sequence
    current_sum = sum(sequence)
    
    # Adjust the last element to ensure the sum equals n
    sequence[-1] += n - current_sum
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))