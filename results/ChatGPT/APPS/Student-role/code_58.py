n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

coloring = [0] * n
color_count = defaultdict(int)
used_colors = defaultdict(set)

for i in range(n):
    num = a[i]
    if color_count[num] < k:
        color_count[num] += 1
        coloring[i] = color_count[num]
        used_colors[num].add(color_count[num])

if len(used_colors) < k:
    print("NO")
else:
    print("YES")
    for i in range(n):
        if coloring[i] == 0:
            for color in range(1, k + 1):
                if color not in used_colors[a[i]]:
                    coloring[i] = color
                    used_colors[a[i]].add(color)
                    break
    print(" ".join(map(str, coloring)))