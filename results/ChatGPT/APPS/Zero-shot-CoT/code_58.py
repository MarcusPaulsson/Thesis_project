n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

coloring = [0] * n
frequency = defaultdict(list)

# Store the indices of each unique number in the array
for i in range(n):
    frequency[a[i]].append(i)

# If any number occurs more than k times, it's impossible to color it
if any(len(indices) > k for indices in frequency.values()):
    print("NO")
else:
    print("YES")
    current_color = 1
    # Assign colors to each index based on the frequency list
    for indices in frequency.values():
        for idx in indices:
            coloring[idx] = current_color
            current_color += 1
            if current_color > k:
                current_color = 1

    print(" ".join(map(str, coloring)))