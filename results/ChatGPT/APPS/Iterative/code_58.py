n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

color_map = defaultdict(list)
for index, value in enumerate(a):
    color_map[value].append(index)

# Check if any number appears more than k times
if any(len(indices) > k for indices in color_map.values()):
    print("NO")
else:
    color_assignment = [0] * n

    for value, indices in color_map.items():
        for i, index in enumerate(indices):
            color_assignment[index] = (i % k) + 1  # Color from 1 to k

    print("YES")
    print(" ".join(map(str, color_assignment)))