def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Step 1: Create a mapping of characters to their positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # Step 2: Create a list to store the color for each character
    colors = [0] * n
    color_count = 0

    # Step 3: Assign colors based on the positions of characters
    for char in sorted(char_positions.keys()):
        positions = char_positions[char]
        current_color = 1
        for pos in positions:
            # If the current position can be colored with the same color as the last one
            if pos > 0 and s[pos] == s[pos - 1]:
                colors[pos] = colors[pos - 1]
            else:
                colors[pos] = current_color
                current_color += 1
                color_count = max(color_count, current_color - 1)

    return color_count, colors

# Input reading
n = int(input().strip())
s = input().strip()

# Get the result
result_color_count, result_colors = min_colors_to_sort(n, s)

# Output the result
print(result_color_count)
print(' '.join(map(str, result_colors)))