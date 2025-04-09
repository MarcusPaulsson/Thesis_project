n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Current distance
current_distance = abs(min_index - max_index)

# Possible new distances after one swap
new_distance1 = abs(min_index - (n - 1))  # Swap 1 with last element
new_distance2 = abs(min_index - 0)        # Swap 1 with first element
new_distance3 = abs(max_index - (n - 1))  # Swap n with last element
new_distance4 = abs(max_index - 0)        # Swap n with first element

# Calculate maximum possible distance
max_distance = max(current_distance, new_distance1, new_distance2, new_distance3, new_distance4)

print(max_distance)