n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate the current distance
current_distance = abs(min_index - max_index)

# The maximum possible distance after one swap could be:
max_distance = max(min_index + (n - 1 - max_index), (n - 1 - min_index) + max_index)

# The result is the maximum of current distance and max_distance
result = max(current_distance, max_distance)
print(result)