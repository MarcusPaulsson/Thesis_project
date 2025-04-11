def min_colors_to_sort(n, s):
    from collections import defaultdict
    
    # Step 1: Create a mapping of character positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)
    
    # Step 2: Create a list of colors
    colors = [0] * n
    color_count = 0
    
    # Step 3: Iterate through the characters in sorted order
    sorted_chars = sorted(char_positions.keys())
    for char in sorted_chars:
        positions = char_positions[char]
        # Assign a new color for each group of positions
        for i in range(len(positions)):
            if i == 0:
                color_count += 1
            colors[positions[i]] = color_count
    
    # Step 4: Output the result
    print(color_count)
    print(' '.join(map(str, colors)))

# Input reading
n = int(input().strip())
s = input().strip()
min_colors_to_sort(n, s)