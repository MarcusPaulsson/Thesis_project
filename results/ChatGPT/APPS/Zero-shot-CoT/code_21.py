n = int(input())
a = list(map(int, input().split()))

# Find the positions of the minimum and maximum elements
min_index = a.index(1)
max_index = a.index(n)

# Calculate the current distance
current_distance = abs(min_index - max_index)

# The maximum possible distance will either be to swap min with the ends or max with the ends
max_distance = max(min_index, max_index, n - 1 - min_index, n - 1 - max_index)

# The result is the maximum of current distance and potential maximum distance
print(max(max_distance, current_distance))