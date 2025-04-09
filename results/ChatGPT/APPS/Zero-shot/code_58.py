n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

# Dictionary to store the indices of each number
num_indices = defaultdict(list)
for i in range(n):
    num_indices[a[i]].append(i)

# Check if there are more unique numbers than colors
if len(num_indices) > k:
    print("NO")
    exit()

# Prepare the color assignment
color_assignment = [0] * n
current_color = 1

# Assign colors
for indices in num_indices.values():
    for index in indices:
        color_assignment[index] = current_color
        current_color += 1
        if current_color > k:
            current_color = 1

# If we have filled all colors, we can just distribute the remaining colors
for i in range(n):
    if color_assignment[i] == 0:
        color_assignment[i] = current_color
        current_color += 1
        if current_color > k:
            current_color = 1

print("YES")
print(" ".join(map(str, color_assignment)))