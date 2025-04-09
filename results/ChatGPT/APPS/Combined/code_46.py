def count_divisible_pairs(n, m):
    # Count occurrences of each remainder when divided by 5
    count_x = [0] * 5
    count_y = [0] * 5
    
    # Count remainders for numbers from 1 to n
    for i in range(1, n + 1):
        count_x[i % 5] += 1
    
    # Count remainders for numbers from 1 to m
    for j in range(1, m + 1):
        count_y[j % 5] += 1
    
    # Calculate the number of valid pairs
    total_pairs = 0
    for i in range(5):
        total_pairs += count_x[i] * count_y[(5 - i) % 5]
    
    return total_pairs

# Read input
n, m = map(int, input().split())
# Output the result
print(count_divisible_pairs(n, m))