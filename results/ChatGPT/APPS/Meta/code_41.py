def nearest_zero_distance(n, a):
    distances = [float('inf')] * n
    
    # First pass: from left to right
    last_zero_index = -1
    for i in range(n):
        if a[i] == 0:
            last_zero_index = i
        if last_zero_index != -1:
            distances[i] = i - last_zero_index
    
    # Second pass: from right to left
    last_zero_index = -1
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            last_zero_index = i
        if last_zero_index != -1:
            distances[i] = min(distances[i], last_zero_index - i)
    
    return distances

# Input reading
n = int(input())
a = list(map(int, input().split()))

# Get the distances
result = nearest_zero_distance(n, a)

# Print the result
print(' '.join(map(str, result)))