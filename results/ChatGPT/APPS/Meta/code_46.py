def count_divisible_pairs(n, m):
    # Count how many numbers in the range 1 to n have each remainder when divided by 5
    count_x = [0] * 5
    for i in range(1, n + 1):
        count_x[i % 5] += 1

    # Count how many numbers in the range 1 to m have each remainder when divided by 5
    count_y = [0] * 5
    for j in range(1, m + 1):
        count_y[j % 5] += 1

    # Calculate the number of valid pairs (x, y) such that (x + y) % 5 == 0
    result = 0
    for i in range(5):
        result += count_x[i] * count_y[(5 - i) % 5]

    return result

# Read input
n, m = map(int, input().split())
# Print the result
print(count_divisible_pairs(n, m))