def find_sequence(n, k):
    if k * (k + 1) // 2 > n:
        return -1
    
    # Maximum GCD we can use
    g = n // k
    
    # Calculate the smallest sequence
    sequence = [i for i in range(1, k + 1)]
    
    # Calculate the sum of the smallest sequence
    sum_sequence = sum(sequence)
    
    # Calculate the excess that needs to be added to the sequence
    excess = n - sum_sequence
    
    # If there's an excess, distribute it to maximize the GCD
    for i in range(k):
        add = excess // k
        sequence[i] += add
        excess -= add
    
    # Distribute any remaining excess one by one
    for i in range(k):
        if excess > 0:
            sequence[i] += 1
            excess -= 1
    
    # Scale the sequence by the calculated GCD
    g = n // sum(sequence)
    scaled_sequence = [x * g for x in sequence]
    
    return scaled_sequence

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))