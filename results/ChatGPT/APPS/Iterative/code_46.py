def count_pairs(n, m):
    # Count occurrences of each remainder when divided by 5
    count_x = [0] * 5
    count_y = [0] * 5

    # Count occurrences of remainders for numbers from 1 to n
    for i in range(1, n + 1):
        count_x[i % 5] += 1

    # Count occurrences of remainders for numbers from 1 to m
    for j in range(1, m + 1):
        count_y[j % 5] += 1

    # Count valid pairs (x, y) such that (x + y) % 5 == 0
    result = 0
    for i in range(5):
        result += count_x[i] * count_y[(5 - i) % 5]

    return result

# Input
n, m = map(int, input().split())
# Output
print(count_pairs(n, m))