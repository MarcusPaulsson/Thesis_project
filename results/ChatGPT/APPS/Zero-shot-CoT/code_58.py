n, k = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

# Count the frequency of each number
frequency = defaultdict(int)
for number in a:
    frequency[number] += 1

# If any number appears more than k times, it's impossible
if any(count > k for count in frequency.values()):
    print("NO")
else:
    print("YES")
    
    # Prepare the coloring
    color_assignment = [0] * n
    current_color = 1
    used_colors = defaultdict(list)

    for i in range(n):
        number = a[i]
        if len(used_colors[number]) < k:
            color_assignment[i] = current_color
            used_colors[number].append(current_color)
            current_color += 1
            if current_color > k:
                current_color = 1
        else:
            # If all colors for this number are used, reuse the first color
            color_assignment[i] = used_colors[number][0]

    print(" ".join(map(str, color_assignment)))