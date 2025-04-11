n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate the current distance
current_distance = abs(min_index - max_index)

# Calculate the maximum possible distance after one swap
max_distance = max(min_index, max_index, n - 1 - min_index, n - 1 - max_index)

# The maximum distance we can achieve is either the current distance or the new maximum distance
result = max(current_distance, max_distance)

print(result)