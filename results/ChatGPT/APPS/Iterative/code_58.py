n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

# Dictionary to hold the indices of each number
indices = defaultdict(list)

for index, value in enumerate(a):
    indices[value].append(index)

# Check if we can color the array
if len(indices) > k:
    print("NO")
else:
    print("YES")
    color = [0] * n
    current_color = 1
    
    # Assign colors while ensuring distinct colors for each number
    for value, index_list in indices.items():
        for index in index_list:
            color[index] = current_color
        current_color += 1
        if current_color > k:
            current_color = 1

    # Ensure all colors from 1 to k are used at least once
    used_colors = set(color)
    if len(used_colors) < k:
        print("NO")
    else:
        print(" ".join(map(str, color)))