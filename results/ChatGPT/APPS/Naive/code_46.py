def count_divisible_pairs(n, m):
    count_x = [0] * 5
    count_y = [0] * 5
    
    # Count occurrences of each remainder for x from 1 to n
    for i in range(1, n + 1):
        count_x[i % 5] += 1
        
    # Count occurrences of each remainder for y from 1 to m
    for j in range(1, m + 1):
        count_y[j % 5] += 1
        
    # Calculate the number of valid pairs
    result = 0
    for k in range(5):
        result += count_x[k] * count_y[(5 - k) % 5]
    
    return result

# Input reading
n, m = map(int, input().split())
# Output the result
print(count_divisible_pairs(n, m))