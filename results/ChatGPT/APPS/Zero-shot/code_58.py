n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

# Store the indices of each unique number
index_map = defaultdict(list)
for idx, value in enumerate(a):
    index_map[value].append(idx)

# If we have more unique numbers than colors, it's impossible
if len(index_map) > k:
    print("NO")
    exit()

# Prepare the result array
result = [0] * n
color = 1

# Assign colors to elements
for indices in index_map.values():
    for i, idx in enumerate(indices):
        result[idx] = (i % k) + 1

# Output result
print("YES")
print(" ".join(map(str, result)))