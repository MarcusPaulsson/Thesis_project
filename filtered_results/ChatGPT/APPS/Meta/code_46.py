def count_divisible_pairs(n, m):
    count_x = [0] * 5
    count_y = [0] * 5
    
    # Count occurrences of remainders for x in range 1 to n
    for i in range(1, n + 1):
        count_x[i % 5] += 1
    
    # Count occurrences of remainders for y in range 1 to m
    for j in range(1, m + 1):
        count_y[j % 5] += 1
    
    # Calculate the number of valid pairs
    result = 0
    for i in range(5):
        result += count_x[i] * count_y[(5 - i) % 5]
    
    return result

# Read input
n, m = map(int, input().split())
print(count_divisible_pairs(n, m))