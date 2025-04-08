def minimum_colors_to_sort(n, s):
    # Create a list to store the color for each character
    colors = [0] * n
    # A dictionary to store the last positions of each character
    last_position = {}
    
    # The number of unique colors used
    current_color = 1

    for i in range(n):
        char = s[i]
        if char in last_position:
            # If the character was seen before, assign the same color
            colors[i] = colors[last_position[char]]
        else:
            # If it's a new character, assign a new color
            colors[i] = current_color
            current_color += 1
        
        last_position[char] = i

    # The number of unique colors used
    unique_colors = current_color - 1
    
    return unique_colors, colors

# Input reading
n = int(input().strip())
s = input().strip()

# Get the result
result, coloring = minimum_colors_to_sort(n, s)

# Output the result
print(result)
print(" ".join(map(str, coloring)))