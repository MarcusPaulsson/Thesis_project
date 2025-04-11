def nearest_zero_distance(n, array):
    distances = [float('inf')] * n
    last_zero_index = -1

    # Forward pass to find distances to the nearest zero
    for i in range(n):
        if array[i] == 0:
            last_zero_index = i
            distances[i] = 0
        elif last_zero_index != -1:
            distances[i] = i - last_zero_index

    # Backward pass to find distances to the nearest zero
    last_zero_index = -1
    for i in range(n - 1, -1, -1):
        if array[i] == 0:
            last_zero_index = i
        elif last_zero_index != -1:
            distances[i] = min(distances[i], last_zero_index - i)

    return distances

# Example usage:
n = int(input())
array = list(map(int, input().split()))
result = nearest_zero_distance(n, array)
print(' '.join(map(str, result)))