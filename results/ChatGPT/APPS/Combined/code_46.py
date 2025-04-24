def count_divisible_pairs(n, m):
    count_x = [0] * 5
    count_y = [0] * 5
    
    for i in range(1, n + 1):
        count_x[i % 5] += 1
        
    for j in range(1, m + 1):
        count_y[j % 5] += 1
        
    result = sum(count_x[i] * count_y[(5 - i) % 5] for i in range(5))
    
    return result

n, m = map(int, input().split())
print(count_divisible_pairs(n, m))