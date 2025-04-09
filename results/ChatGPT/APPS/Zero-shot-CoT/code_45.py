def find_sequence(n, k):
    if n < (k * (k + 1)) // 2:
        return -1

    # The maximum possible gcd we can have is n // k
    max_gcd = n // k

    # The resulting sequence
    sequence = [(i + 1) * max_gcd for i in range(k)]
    
    # Adjust the last element to make sure the sum equals to n
    sequence[-1] += n - sum(sequence)

    return sequence

# Read input
n, k = map(int, input().split())

# Find the sequence
result = find_sequence(n, k)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))