def find_sequence(n, k):
    # Check if it's possible to form a strictly increasing sequence of k positive integers that sum to n
    if n < k * (k + 1) // 2:
        return -1
    
    # Start with the smallest k integers
    sequence = list(range(1, k + 1))
    sum_sequence = sum(sequence)
    
    # Calculate the excess we need to distribute
    excess = n - sum_sequence
    
    # Distribute the excess evenly to maximize the GCD
    # The maximum GCD we can achieve is the excess plus 1 divided by k
    max_gcd = (excess // k) + 1
    
    # Increase each element in the sequence by max_gcd
    sequence = [x + max_gcd for x in sequence]
    
    # Adjust the last element to ensure the sum is exactly n
    sequence[-1] += excess - (max_gcd * k)
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))