def find_sequence(n, k):
    # Minimum sum of the first k positive integers is k * (k + 1) / 2
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1  # Not enough sum to create the sequence
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # We will create the sequence using the maximum possible GCD
    # Start with the first k integers multiplied by max_gcd
    a = [(i + 1) * max_gcd for i in range(k)]
    
    # Calculate the sum of this sequence
    current_sum = sum(a)
    
    # Adjust the last element to make sure the sum equals n
    a[-1] += (n - current_sum)
    
    # If the last element makes the sequence not strictly increasing, we need to check
    if a[-1] <= a[-2]:
        return -1
    
    return a

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))