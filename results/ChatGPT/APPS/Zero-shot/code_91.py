n = int(input())
a = list(map(int, input().split()))

# Initialize distance array with large values
distance = [float('inf')] * n

# Forward pass to find distances to the nearest zero on the left
for i in range(n):
    if a[i] == 0:
        distance[i] = 0
    elif i > 0:
        distance[i] = distance[i - 1] + 1

# Backward pass to find distances to the nearest zero on the right
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        distance[i] = 0
    elif i < n - 1:
        distance[i] = min(distance[i], distance[i + 1] + 1)

print(' '.join(map(str, distance)))