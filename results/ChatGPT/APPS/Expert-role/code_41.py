def nearest_zero_distance(n, a):
    distances = [float('inf')] * n
    last_zero = -1

    # Forward pass to find distances to the nearest zero
    for i in range(n):
        if a[i] == 0:
            last_zero = i
            distances[i] = 0
        elif last_zero != -1:
            distances[i] = i - last_zero

    # Backward pass to find distances to the nearest zero
    last_zero = -1
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last_zero = i
        elif last_zero != -1:
            distances[i] = min(distances[i], last_zero - i)

    return distances

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Get the result and print it
result = nearest_zero_distance(n, a)
print(' '.join(map(str, result)))