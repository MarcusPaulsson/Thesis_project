def find_sequence(n, k):
    # Minimum sum of first k natural numbers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum gcd we can use is n // k
    max_gcd = n // k
    
    # We will try to find the sequence
    for g in range(max_gcd, 0, -1):
        # Calculate the sum we need to reach with the sequence
        target_sum = n // g
        
        # Check if we can form the sequence with the current gcd
        if target_sum >= min_sum:
            # Create the sequence
            sequence = [(i + 1) * g for i in range(k)]
            return sequence
    
    return -1

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))