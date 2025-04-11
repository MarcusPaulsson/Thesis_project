n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

# Count occurrences of each number
count = defaultdict(int)
for num in a:
    count[num] += 1

# If any number occurs more than k times, it's impossible
if any(c > k for c in count.values()):
    print("NO")
    exit()

# Prepare to assign colors
color_assignment = [0] * n
color_used = defaultdict(int)

# Assign colors
for i in range(n):
    num = a[i]
    color_used[num] += 1
    color_assignment[i] = color_used[num] if color_used[num] <= k else 0

# Check if we have assigned all colors
if any(c == 0 for c in color_assignment):
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, color_assignment)))