def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Create a mapping of character positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # Create a list to store the color for each character
    colors = [0] * n
    color_count = 0

    # Create a list of the characters sorted
    sorted_chars = sorted(char_positions.keys())

    # Assign colors based on the sorted order
    for char in sorted_chars:
        positions = char_positions[char]
        # Assign a new color for this character
        color_count += 1
        for pos in positions:
            colors[pos] = color_count

    return color_count, colors

# Read input
n = int(input())
s = input().strip()

# Get the result
res, coloring = min_colors_to_sort(n, s)

# Print the output
print(res)
print(' '.join(map(str, coloring)))