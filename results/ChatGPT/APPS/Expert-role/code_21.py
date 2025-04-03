n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate the current distance
current_distance = abs(min_index - max_index)

# Possible new positions after swaps
new_positions = [
    abs(min_index - 0),        # Swap with first element
    abs(min_index - (n - 1)),  # Swap with last element
    abs(max_index - 0),        # Swap with first element
    abs(max_index - (n - 1))   # Swap with last element
]

# The maximum possible distance after one swap
max_distance = max(new_positions)

print(max(max_distance, current_distance))