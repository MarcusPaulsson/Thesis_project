def create_sequence(n, k):
    min_required_sum = k * (k + 1) // 2
    if min_required_sum > n:
        return -1
    
    # Start with the maximum GCD and create the initial sequence
    max_gcd = n // k
    sequence = [max_gcd * i for i in range(1, k + 1)]
    
    # Calculate the current sum of the sequence
    current_sum = sum(sequence)
    
    # Calculate the difference needed to reach the target sum
    difference = n - current_sum
    
    # If the difference is non-negative, adjust the last element
    if difference >= 0:
        sequence[-1] += difference
        return sequence
    else:
        return -1

# Reading input
n, k = map(int, input().split())
result = create_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))