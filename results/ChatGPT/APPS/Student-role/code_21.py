n = int(input())
a = list(map(int, input().split()))

min_index = a.index(1)
max_index = a.index(n)

# Calculate initial distance
initial_distance = abs(min_index - max_index)

# Possible positions for min and max after a swap
new_positions = [
    (0, n - 1),  # swap min with first element or max with last element
    (n - 1, 0)   # swap max with first element or min with last element
]

max_distance = initial_distance

for min_pos, max_pos in new_positions:
    new_min_index = min_pos if a[min_pos] == 1 else max_index
    new_max_index = max_pos if a[max_pos] == n else min_index
    max_distance = max(max_distance, abs(new_min_index - new_max_index))

print(max_distance)