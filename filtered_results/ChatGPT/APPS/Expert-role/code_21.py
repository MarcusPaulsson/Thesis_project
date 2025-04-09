n = int(input())
a = list(map(int, input().split()))

# Find the positions of the minimum (1) and maximum (n) elements
min_pos = a.index(1)
max_pos = a.index(n)

# Calculate the current distance
current_distance = abs(min_pos - max_pos)

# Calculate potential new distances after performing one swap
# Swap min with the first element or the last element
distance_if_swap_first = abs(0 - max_pos)  # Swap min (1) with a[0]
distance_if_swap_last = abs(n - 1 - max_pos)  # Swap min (1) with a[n-1]

# Swap max with the first element or the last element
distance_if_swap_min_first = abs(min_pos - 0)  # Swap max (n) with a[0]
distance_if_swap_min_last = abs(min_pos - (n - 1))  # Swap max (n) with a[n-1]

# The maximum possible distance after one swap
max_distance = max(current_distance, distance_if_swap_first, distance_if_swap_last,
                   distance_if_swap_min_first, distance_if_swap_min_last)

print(max_distance)