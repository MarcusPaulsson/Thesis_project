def nearest_zero_distance(n, arr):
    distances = [0] * n
    last_zero_index = -1
    
    # Forward pass to find distances to the nearest zero on the left
    for i in range(n):
        if arr[i] == 0:
            last_zero_index = i
            distances[i] = 0
        else:
            if last_zero_index != -1:
                distances[i] = i - last_zero_index
    
    last_zero_index = -1
    
    # Backward pass to find distances to the nearest zero on the right
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            last_zero_index = i
        else:
            if last_zero_index != -1:
                distances[i] = min(distances[i], last_zero_index - i)
    
    return distances

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Get the result
result = nearest_zero_distance(n, arr)

# Print the result
print(" ".join(map(str, result)))