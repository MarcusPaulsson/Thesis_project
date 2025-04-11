n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

coloring = [0] * n
count = defaultdict(int)

# Track the used colors for each number
used_colors = defaultdict(set)

# Assign colors
for i in range(n):
    num = a[i]
    # Find the first available color for this number
    for color in range(1, k + 1):
        if color not in used_colors[num]:
            coloring[i] = color
            used_colors[num].add(color)
            count[color] += 1
            break

# Check if we have at least one of each color
if len(count) < k:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, coloring)))