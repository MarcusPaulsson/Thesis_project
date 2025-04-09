def count_pairs(n, m):
    # Count occurrences of remainders when divided by 5
    count_n = [0] * 5
    count_m = [0] * 5
    
    for i in range(1, n + 1):
        count_n[i % 5] += 1
        
    for j in range(1, m + 1):
        count_m[j % 5] += 1
        
    # Calculate pairs where (x + y) % 5 == 0
    result = 0
    for i in range(5):
        result += count_n[i] * count_m[(5 - i) % 5]
    
    return result

# Reading input
n, m = map(int, input().split())
print(count_pairs(n, m))