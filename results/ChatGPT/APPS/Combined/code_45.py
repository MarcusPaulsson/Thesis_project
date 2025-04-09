def find_sequence(n, k):
    # The minimum sum of the first k positive integers
    min_required_sum = k * (k + 1) // 2
    
    # If n is less than the minimum required sum, return -1
    if n < min_required_sum:
        return -1

    # Calculate the maximum GCD we can start with
    max_gcd = n // k
    
    # Adjust the GCD downwards until the sequence is valid
    while True:
        # Calculate the sum of the sequence with the current GCD
        sum_sequence = max_gcd * min_required_sum
        
        if sum_sequence <= n:
            # Create the sequence with the current GCD
            sequence = [max_gcd * i for i in range(1, k + 1)]
            sequence[-1] += (n - sum_sequence)  # Adjust the last element
            return sequence
        max_gcd -= 1  # Decrease GCD if the sum exceeds n

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))