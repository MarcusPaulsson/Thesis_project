def count_pairs(n, m):
    counts_x = [0] * 5
    counts_y = [0] * 5
    
    # Count occurrences of each remainder for x
    for i in range(1, n + 1):
        counts_x[i % 5] += 1
    
    # Count occurrences of each remainder for y
    for i in range(1, m + 1):
        counts_y[i % 5] += 1
    
    # Calculate pairs where (x + y) % 5 == 0
    total_pairs = 0
    for i in range(5):
        total_pairs += counts_x[i] * counts_y[(5 - i) % 5]
    
    return total_pairs

# Input reading
n, m = map(int, input().split())
print(count_pairs(n, m))