def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Create a mapping of character positions
    char_positions = defaultdict(list)
    for i, char in enumerate(s):
        char_positions[char].append(i)

    # Create a list to store the color for each character
    colors = [0] * n
    color = 1

    # Iterate through the characters in sorted order
    for char in sorted(char_positions.keys()):
        positions = char_positions[char]
        # Assign the same color to all occurrences of the character
        for pos in positions:
            colors[pos] = color
        color += 1

    # The number of colors used is the last color - 1
    num_colors = color - 1

    return num_colors, colors

# Input reading
n = int(input())
s = input().strip()

# Get the result
num_colors, coloring = min_colors_to_sort(n, s)

# Output the result
print(num_colors)
print(' '.join(map(str, coloring)))