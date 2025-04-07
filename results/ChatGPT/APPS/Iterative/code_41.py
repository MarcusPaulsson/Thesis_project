n = int(input())
a = list(map(int, input().split()))

# Initialize the distance array with a large value
distances = [float('inf')] * n

# First pass: left to right
last_zero = -1
for i in range(n):
    if a[i] == 0:
        last_zero = i
    if last_zero != -1:
        distances[i] = i - last_zero

# Second pass: right to left
last_zero = -1
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last_zero = i
    if last_zero != -1:
        distances[i] = min(distances[i], last_zero - i)

print(' '.join(map(str, distances)))