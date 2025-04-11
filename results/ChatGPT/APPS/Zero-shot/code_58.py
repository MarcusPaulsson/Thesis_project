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

# Prepare to color the elements
color = [0] * n
current_color = 1
used_colors = defaultdict(int)

for i in range(n):
    num = a[i]
    # Assign a color to the current number
    if used_colors[num] < k:
        color[i] = (used_colors[num] + 1)
        used_colors[num] += 1
    else:
        # If we have used all colors for this number, we need to cycle through colors
        color[i] = (used_colors[num] % k) + 1
        used_colors[num] += 1

# Check if we have used all colors at least once
if len(set(color)) < k:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, color)))