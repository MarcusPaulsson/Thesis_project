def min_colors_to_sort(n, s):
    from collections import defaultdict
    
    # Step 1: Create a mapping of character positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)
    
    # Step 2: Create a list to store colors
    colors = [0] * n
    color_count = 0
    
    # Step 3: Assign colors based on the positions of characters
    for char in sorted(char_positions.keys()):
        positions = char_positions[char]
        current_color = 1
        
        for pos in positions:
            colors[pos] = current_color
            
            # If the next character is the same, keep the same color
            if current_color < color_count:
                current_color += 1
        
        # Update the color count
        color_count = max(color_count, current_color)
    
    return color_count, colors

# Input reading
n = int(input())
s = input().strip()

# Get the result
result_color_count, result_colors = min_colors_to_sort(n, s)

# Output the result
print(result_color_count)
print(' '.join(map(str, result_colors)))