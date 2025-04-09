def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Create a list of positions for each character
    positions = defaultdict(list)
    for index, char in enumerate(s):
        positions[char].append(index)
    
    # Determine the number of colors needed
    max_color = 1
    coloring = [0] * n
    color_map = {}

    for char in sorted(positions.keys()):  # Process characters in alphabetical order
        indices = positions[char]
        current_color = max_color

        for idx in indices:
            if coloring[idx] == 0:  # If not colored yet
                coloring[idx] = current_color
                
        max_color += 1  # Increment color for the next character

    # We need to adjust the colors to ensure we can sort via swaps
    color_to_use = [0] * (max_color - 1)
    for i in range(n):
        color_to_use[coloring[i] - 1] = max(color_to_use[coloring[i] - 1], coloring[i])

    # Finalize the coloring
    final_color = []
    for i in range(n):
        final_color.append(color_to_use[coloring[i] - 1])

    print(max_color - 1)
    print(' '.join(map(str, final_color)))

# Example inputs
n = int(input().strip())
s = input().strip()
min_colors_to_sort(n, s)