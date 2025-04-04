n = int(input())
array = list(map(int, input().split()))

# Initialize the distance array with a large number
distances = [float('inf')] * n

# First pass: from left to right
for i in range(n):
    if array[i] == 0:
        distances[i] = 0
    elif i > 0:
        distances[i] = distances[i - 1] + 1

# Second pass: from right to left
for i in range(n - 1, -1, -1):
    if array[i] == 0:
        distances[i] = 0
    elif i < n - 1:
        distances[i] = min(distances[i], distances[i + 1] + 1)

print(' '.join(map(str, distances)))