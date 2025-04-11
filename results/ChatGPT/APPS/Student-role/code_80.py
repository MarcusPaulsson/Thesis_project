def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Step 1: Create a mapping of characters to their positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # Step 2: Create a list to hold the color assignments
    colors = [0] * n
    current_color = 1

    # Step 3: Assign colors based on the positions of characters
    for char in sorted(char_positions.keys()):
        positions = char_positions[char]
        for i in range(len(positions)):
            colors[positions[i]] = (i % current_color) + 1
        current_color = max(current_color, len(positions))

    # Step 4: Output the results
    print(current_color)
    print(' '.join(map(str, colors)))

# Example usage
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)