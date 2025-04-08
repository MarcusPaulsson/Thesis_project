def count_divisible_pairs(n, m):
    # Initialize counts for remainders when divided by 5
    count_x = [0] * 5
    count_y = [0] * 5

    # Count occurrences of each remainder in range 1 to n
    for i in range(1, n + 1):
        count_x[i % 5] += 1

    # Count occurrences of each remainder in range 1 to m
    for j in range(1, m + 1):
        count_y[j % 5] += 1

    # Calculate total pairs where (x + y) % 5 == 0
    total_pairs = (
        count_x[0] * count_y[0] + 
        count_x[1] * count_y[4] + 
        count_x[2] * count_y[3] + 
        count_x[3] * count_y[2] + 
        count_x[4] * count_y[1]
    )

    return total_pairs

# Read input values for n and m
n, m = map(int, input().split())
# Output the result
print(count_divisible_pairs(n, m))