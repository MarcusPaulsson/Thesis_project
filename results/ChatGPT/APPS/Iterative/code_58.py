n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

coloring = [0] * n
color_used = defaultdict(list)

for i in range(n):
    color_used[a[i]].append(i)

if len(color_used) < k:
    print("NO")
else:
    color = 1
    for indices in color_used.values():
        if len(indices) < k:
            # If there are not enough distinct colors available for this group
            for index in indices:
                coloring[index] = color
                color = (color % k) + 1
        else:
            # Assign colors from 1 to k for the first k distinct elements
            for j in range(k):
                coloring[indices[j]] = j + 1
            # Continue coloring the rest with the available colors
            for index in indices[k:]:
                coloring[index] = (j + 1) % k + 1

    print("YES")
    print(" ".join(map(str, coloring)))