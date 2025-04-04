def nearest_zero_distance(n, array):
    distances = [float('inf')] * n
    last_zero_index = -1

    # First pass: from left to right
    for i in range(n):
        if array[i] == 0:
            last_zero_index = i
            distances[i] = 0
        elif last_zero_index != -1:
            distances[i] = i - last_zero_index

    # Second pass: from right to left
    last_zero_index = -1
    for i in range(n - 1, -1, -1):
        if array[i] == 0:
            last_zero_index = i
        elif last_zero_index != -1:
            distances[i] = min(distances[i], last_zero_index - i)

    return distances

# Input reading
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Get distances to the nearest zero and print them
result = nearest_zero_distance(n, array)
print(' '.join(map(str, result)))