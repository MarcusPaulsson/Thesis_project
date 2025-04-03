def find_sequence(n, k):
    if k * (k + 1) // 2 > n:
        return -1
    
    # Calculate the maximum gcd that can be used
    max_gcd = n // k
    
    # Start with the minimum increasing sequence {1, 2, ..., k}
    seq = list(range(1, k + 1))
    
    # Calculate the sum of the initial sequence
    current_sum = sum(seq)
    
    # Calculate the difference needed to reach n
    difference = n - current_sum
    
    # Distribute the difference evenly to maximize gcd
    if difference > 0:
        # We can increase each element by the same amount
        # We can add `difference // k` to each element
        add = difference // k
        for i in range(k):
            seq[i] += add
        
        # If there's any remainder, we can distribute it starting from the last element
        remainder = difference % k
        for i in range(k - 1, k - 1 - remainder, -1):
            seq[i] += 1
    
    return seq

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))