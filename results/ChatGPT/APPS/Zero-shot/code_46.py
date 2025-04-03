n, m = map(int, input().split())

# Count how many numbers in the range 1 to n give each remainder when divided by 5
count_x = [0] * 5
for i in range(1, n + 1):
    count_x[i % 5] += 1

# Count how many numbers in the range 1 to m give each remainder when divided by 5
count_y = [0] * 5
for j in range(1, m + 1):
    count_y[j % 5] += 1

# Calculate the number of valid pairs (x, y)
result = 0
for r in range(5):
    result += count_x[r] * count_y[(5 - r) % 5]

print(result)