n = int(input())
a = list(map(int, input().split()))

distances = [0] * n
last_zero_index = -1

# Forward pass to find distances to the nearest zero on the left
for i in range(n):
    if a[i] == 0:
        last_zero_index = i
        distances[i] = 0
    else:
        if last_zero_index != -1:
            distances[i] = i - last_zero_index

# Backward pass to find distances to the nearest zero on the right
last_zero_index = -1
for i in range(n - 1, -1, -1):
    if a[i] == 0:
        last_zero_index = i
    else:
        if last_zero_index != -1:
            distances[i] = min(distances[i], last_zero_index - i)

print(' '.join(map(str, distances)))