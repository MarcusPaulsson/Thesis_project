def count_divisible_pairs(n, m):
    count_x = [0] * 5
    count_y = [0] * 5
    
    # Count how many numbers in range 1 to n give each remainder when divided by 5
    for i in range(1, n + 1):
        count_x[i % 5] += 1
    
    # Count how many numbers in range 1 to m give each remainder when divided by 5
    for j in range(1, m + 1):
        count_y[j % 5] += 1
    
    # Calculate pairs where (x + y) % 5 == 0
    total_pairs = 0
    for r in range(5):
        total_pairs += count_x[r] * count_y[(5 - r) % 5]
    
    return total_pairs

# Input reading
n, m = map(int, input().split())
result = count_divisible_pairs(n, m)
print(result)