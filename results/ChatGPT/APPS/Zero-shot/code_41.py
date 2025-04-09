n = int(input())
a = list(map(int, input().split()))

# Initialize the distance array with a large value
distances = [float('inf')] * n

# First pass: left to right
for i in range(n):
    if a[i] == 0:
        distances[i] = 0
    elif i > 0:
        distances[i] = distances[i - 1] + 1

# Second pass: right to left
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        distances[i] = 0
    elif i < n - 1:
        distances[i] = min(distances[i], distances[i + 1] + 1)

print(" ".join(map(str, distances)))