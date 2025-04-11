def count_divisible_pairs(n, m):
    # Count occurrences of each remainder when divided by 5
    count_x = [0] * 5
    count_y = [0] * 5

    # Count how many numbers in range 1 to n give each remainder when divided by 5
    for i in range(1, n + 1):
        count_x[i % 5] += 1

    # Count how many numbers in range 1 to m give each remainder when divided by 5
    for j in range(1, m + 1):
        count_y[j % 5] += 1

    # Calculate the number of valid pairs
    total_pairs = sum(count_x[r] * count_y[(5 - r) % 5] for r in range(5))

    return total_pairs

# Read input
n, m = map(int, input().split())
# Print the result
print(count_divisible_pairs(n, m))