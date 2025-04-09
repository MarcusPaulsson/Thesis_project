n, m = map(int, input().split())

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
result = (count_x[0] * count_y[0] + 
          count_x[1] * count_y[4] + 
          count_x[2] * count_y[3] + 
          count_x[3] * count_y[2] + 
          count_x[4] * count_y[1])

print(result)