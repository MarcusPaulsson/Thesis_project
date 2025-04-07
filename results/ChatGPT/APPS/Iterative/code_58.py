n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

coloring = [0] * n
color_used = defaultdict(list)

# Gather indices of each unique element
for i in range(n):
    color_used[a[i]].append(i)

# Check if any element appears more than k times
if any(len(indices) > k for indices in color_used.values()):
    print("NO")
else:
    print("YES")
    current_color = 1
    # Assign colors while ensuring distinctness
    for indices in color_used.values():
        for index in indices:
            coloring[index] = current_color
            current_color += 1
            if current_color > k:
                current_color = 1

    print(" ".join(map(str, coloring)))