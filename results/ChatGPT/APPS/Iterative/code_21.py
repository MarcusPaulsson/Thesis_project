n = int(input())
a = list(map(int, input().split()))

# Find positions of the minimum and maximum elements
min_pos = a.index(1)
max_pos = a.index(n)

# Calculate current distance
current_distance = abs(min_pos - max_pos)

# Potential new positions after swapping
new_distance1 = abs(0 - max_pos)  # Swap min with the first element
new_distance2 = abs(n - 1 - max_pos)  # Swap min with the last element
new_distance3 = abs(min_pos - 0)  # Swap max with the first element
new_distance4 = abs(min_pos - (n - 1))  # Swap max with the last element

# Calculate the maximum distance possible after one swap
max_distance = max(new_distance1, new_distance2, new_distance3, new_distance4)

# Print the result
print(max(max_distance, current_distance))