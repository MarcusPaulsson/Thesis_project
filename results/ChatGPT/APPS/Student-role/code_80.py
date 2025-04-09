n = int(input())
s = input()

from collections import defaultdict

# Create a mapping of characters to their positions
positions = defaultdict(list)
for i, char in enumerate(s):
    positions[char].append(i)

# Colors array
colors = [0] * n
current_color = 1

# Create a list of unique characters sorted
unique_chars = sorted(positions.keys())

# Assign colors based on the positions of characters
for char in unique_chars:
    for i in range(len(positions[char])):
        colors[positions[char][i]] = current_color
        current_color += 1 if i == len(positions[char]) - 1 else 0

# The number of colors used is the max in the colors array
max_color = max(colors)

print(max_color)
print(' '.join(map(str, colors)))