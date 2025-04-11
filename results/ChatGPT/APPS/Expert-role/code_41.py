def nearest_zero_distance(n, a):
    distances = [float('inf')] * n
    last_zero_index = -1

    # Forward pass to find distances to the nearest zero on the left
    for i in range(n):
        if a[i] == 0:
            last_zero_index = i
            distances[i] = 0
        elif last_zero_index != -1:
            distances[i] = i - last_zero_index

    last_zero_index = -1

    # Backward pass to find distances to the nearest zero on the right
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last_zero_index = i
        elif last_zero_index != -1:
            distances[i] = min(distances[i], last_zero_index - i)

    print(' '.join(map(str, distances)))

# Input reading
n = int(input().strip())
a = list(map(int, input().strip().split()))

nearest_zero_distance(n, a)