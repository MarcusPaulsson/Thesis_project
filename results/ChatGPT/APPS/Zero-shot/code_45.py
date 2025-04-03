def find_sequence(n, k):
    if n < k * (k + 1) // 2:  # Minimum sum of first k positive integers
        return -1

    # Maximum GCD we can use
    g = n // k
    # Adjust the numbers based on the GCD
    sequence = [i * g for i in range(1, k + 1)]
    
    # Calculate the remaining sum after using the minimum strictly increasing sequence
    remaining = n - sum(sequence)
    
    # Distribute the remaining value to the last element in the sequence
    sequence[-1] += remaining
    
    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))