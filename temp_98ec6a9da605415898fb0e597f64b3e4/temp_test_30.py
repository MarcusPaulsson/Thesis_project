def min_colors_to_sort(n, s):
    # Create a list to hold the positions of each character
    from collections import defaultdict

    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # Create a list to store the color assignments
    colors = [0] * n
    color = 1
    max_color = 0

    # Assign colors based on the positions
    for char in sorted(char_positions.keys()):
        positions = char_positions[char]
        for i in range(len(positions)):
            colors[positions[i]] = color
            max_color = max(max_color, color)
            if i < len(positions) - 1:
                color += 1

        color = 1  # Reset color for the next character group

    # Output the result
    print(max_color)
    print(' '.join(map(str, colors)))

# Input reading
n = int(input().strip())
s = input().strip()

# Function call
min_colors_to_sort(n, s)