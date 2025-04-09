n = int(input())
a = list(map(int, input().split()))

# Initialize the distances array with a large number
distances = [float('inf')] * n

# Forward pass to find distances from the left
for i in range(n):
    if a[i] == 0:
        distances[i] = 0
    elif i > 0:
        distances[i] = distances[i - 1] + 1

# Backward pass to find distances from the right
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        distances[i] = 0
    else:
        distances[i] = min(distances[i], distances[i + 1] + 1)

print(' '.join(map(str, distances)))