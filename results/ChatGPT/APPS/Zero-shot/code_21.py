n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate initial distance
max_distance = abs(min_index - max_index)

# Check distance if we swap min or max with the ends of the array
distance_with_min_swapped = max(abs(0 - max_index), abs(n - 1 - max_index))
distance_with_max_swapped = max(abs(min_index - 0), abs(min_index - (n - 1)))

# The maximum distance we can achieve
result = max(max_distance, distance_with_min_swapped, distance_with_max_swapped)

print(result)