def nearest_zero_distance(n, array):
    distances = [float('inf')] * n
    last_zero_position = -1

    # First pass: from left to right
    for i in range(n):
        if array[i] == 0:
            last_zero_position = i
            distances[i] = 0
        elif last_zero_position != -1:
            distances[i] = i - last_zero_position

    # Second pass: from right to left
    for i in range(n - 1, -1, -1):
        if array[i] == 0:
            last_zero_position = i
        elif last_zero_position != -1:
            distances[i] = min(distances[i], last_zero_position - i)

    return distances

# Reading input
n = int(input().strip())
array = list(map(int, input().strip().split()))

# Getting distances and printing the result
result = nearest_zero_distance(n, array)
print(" ".join(map(str, result)))