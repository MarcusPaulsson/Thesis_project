n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate initial distance
initial_distance = abs(min_index - max_index)

# Possible new distances after one swap
new_distances = [
    abs(0 - max_index),  # Swap 1 with the first element
    abs(n - 1 - max_index),  # Swap 1 with the last element
    abs(min_index - 0),  # Swap n with the first element
    abs(min_index - (n - 1))  # Swap n with the last element
]

# The maximum distance we can achieve
max_distance = max(new_distances)

# Output the maximum distance
print(max(max_distance, initial_distance))