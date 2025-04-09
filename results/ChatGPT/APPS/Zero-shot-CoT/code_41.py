n = int(input())
a = list(map(int, input().split()))

# Initialize the distance array with a large number
distance = [float('inf')] * n

# Forward pass to find distances to the nearest zero
for i in range(n):
    if a[i] == 0:
        distance[i] = 0
    elif i > 0:
        distance[i] = distance[i - 1] + 1

# Backward pass to find distances to the nearest zero
for i in range(n - 2, -1, -1):
    if distance[i] > distance[i + 1] + 1:
        distance[i] = distance[i + 1] + 1

print(' '.join(map(str, distance)))