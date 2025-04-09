n = int(input())
a = list(map(int, input().split()))

min_pos = a.index(1)
max_pos = a.index(n)

# Initial distance
initial_distance = abs(min_pos - max_pos)

# Calculate potential new distances after one swap
new_distances = [
    abs(0 - max_pos),       # Swap min (1) with the first element
    abs(n - 1 - max_pos),   # Swap min (1) with the last element
    abs(min_pos - 0),       # Swap max (n) with the first element
    abs(min_pos - (n - 1))  # Swap max (n) with the last element
]

# The maximum distance achievable after one swap
max_distance = max(new_distances)

# Print the maximum distance between min and max
print(max(max_distance, initial_distance))