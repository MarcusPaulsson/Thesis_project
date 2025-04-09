def find_sequence(n, k):
    # Check if it's possible to create a sequence of k numbers that sum to n
    if n < (k * (k + 1)) // 2:
        return -1
    
    # Calculate the maximum gcd we can have
    max_gcd = n // k
    
    # Create the sequence with the calculated gcd
    sequence = [(i + 1) * max_gcd for i in range(k)]
    
    # Adjust the last element to ensure the sum equals n
    sequence[-1] += (n - sum(sequence))
    
    # Check if the sequence is strictly increasing and valid
    if sequence[-1] > sequence[-2]:
        return sequence
    else:
        return -1

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))