def find_sequence(n, k):
    # Minimum sum of the first k positive integers
    min_sum = k * (k + 1) // 2
    
    if n < min_sum:
        return -1
    
    # The maximum GCD we can use is n // k
    max_gcd = n // k
    
    # We can construct the sequence
    sequence = [(i + 1) for i in range(k)]
    
    # Calculate the current sum of the sequence
    current_sum = sum(sequence)
    
    # Calculate the difference needed to reach n
    difference = n - current_sum
    
    # Distribute the difference evenly to maximize GCD
    for i in range(k):
        sequence[i] += difference // k
    
    # Distribute any remaining difference to the last elements
    for i in range(difference % k):
        sequence[k - 1 - i] += 1
    
    # Scale the sequence by the maximum GCD
    sequence = [x * max_gcd for x in sequence]
    
    return sequence

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))