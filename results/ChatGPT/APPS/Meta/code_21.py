n = int(input())
a = list(map(int, input().split()))

# Find the positions of the minimum and maximum elements
min_pos = a.index(1)
max_pos = a.index(n)

# Calculate the current distance
current_distance = abs(min_pos - max_pos)

# Calculate the maximum possible distance after one swap
max_distance = max(
    abs(min_pos - 0),  # Swap min with the first element
    abs(min_pos - (n - 1)),  # Swap min with the last element
    abs(max_pos - 0),  # Swap max with the first element
    abs(max_pos - (n - 1))  # Swap max with the last element
)

# The result is the maximum of the current distance and the calculated maximum distance
result = max(current_distance, max_distance)
print(result)