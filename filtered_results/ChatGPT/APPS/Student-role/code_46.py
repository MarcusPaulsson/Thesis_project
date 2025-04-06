def count_pairs(n, m):
    # Count the number of integers in the ranges that give specific remainders when divided by 5
    count_x = [0] * 5
    count_y = [0] * 5
    
    for i in range(1, n + 1):
        count_x[i % 5] += 1
    
    for j in range(1, m + 1):
        count_y[j % 5] += 1

    # Calculate the number of valid pairs
    result = (
        count_x[0] * count_y[0] +  # (0, 0)
        count_x[1] * count_y[4] +  # (1, 4)
        count_x[2] * count_y[3] +  # (2, 3)
        count_x[3] * count_y[2] +  # (3, 2)
        count_x[4] * count_y[1]    # (4, 1)
    )
    
    return result

# Input
n, m = map(int, input().split())
print(count_pairs(n, m))