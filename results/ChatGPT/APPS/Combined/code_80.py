def min_colors_to_sort(n, s):
    from collections import defaultdict

    # Step 1: Identify the positions of each character
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)

    # Step 2: Create a list to hold the colors
    colors = [0] * n
    color_count = 0

    # Step 3: Assign colors based on the positions of characters
    last_color = {}
    for char in sorted(char_positions.keys()):
        color_count += 1
        for pos in char_positions[char]:
            colors[pos] = color_count

    # Step 4: Output the results
    print(color_count)
    print(' '.join(map(str, colors)))

# Example usage
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)