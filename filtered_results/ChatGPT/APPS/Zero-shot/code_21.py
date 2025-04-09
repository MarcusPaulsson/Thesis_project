n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate the current distance
current_distance = abs(min_index - max_index)

# Calculate the potential maximum distances after one swap
distance1 = abs(min_index - (n - 1))  # Swap min with the last element
distance2 = abs(max_index - 0)        # Swap max with the first element
distance3 = abs((n - 1) - max_index)  # Swap max with the last element
distance4 = abs(min_index - 0)        # Swap min with the first element

# The maximum possible distance after one swap
max_distance = max(current_distance, distance1, distance2, distance3, distance4)

print(max_distance)