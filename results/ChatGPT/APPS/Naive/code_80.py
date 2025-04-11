def min_colors_to_sort(n, s):
    # Create a list to store the color assignments
    colors = [0] * n
    # Dictionary to track the last position of each character
    last_position = {}
    
    # Count the number of colors needed
    color_count = 0
    
    for i in range(n):
        char = s[i]
        if char in last_position:
            # If the character has appeared before, assign the same color
            colors[i] = colors[last_position[char]]
        else:
            # New character, increment color count and assign a new color
            color_count += 1
            colors[i] = color_count
        
        # Update the last position of the character
        last_position[char] = i
    
    return color_count, colors

# Input reading
n = int(input().strip())
s = input().strip()

# Get the result
result_count, result_colors = min_colors_to_sort(n, s)

# Output the result
print(result_count)
print(' '.join(map(str, result_colors)))