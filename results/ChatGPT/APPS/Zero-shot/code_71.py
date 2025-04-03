n = int(input())
a = list(map(int, input().split()))

# Find the positions of the minimum (1) and maximum (n) elements
min_pos = a.index(1)
max_pos = a.index(n)

# Calculate the current distance
current_distance = abs(min_pos - max_pos)

# Calculate the possible maximum distances after one swap
max_distance = max(abs(min_pos - 0), abs(min_pos - (n - 1)), abs(max_pos - 0), abs(max_pos - (n - 1)))

# The result is the maximum of the current distance and the possible maximum after one swap
print(max(max_distance, current_distance))