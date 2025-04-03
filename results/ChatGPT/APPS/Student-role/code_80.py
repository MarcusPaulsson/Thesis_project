def min_colors_to_sort(n, s):
    # Create a list to store the colors
    color = [0] * n
    # Create a dictionary to store last positions of each character
    last_position = {}
    
    # Iterate through the string to assign colors
    for i in range(n):
        char = s[i]
        if char in last_position:
            # Determine the color to use for this character
            color[i] = (last_position[char] + 1) % (max_color + 1)
        else:
            color[i] = 1  # Start new color
        last_position[char] = color[i]  # Update last position for this character

    # Calculate the maximum color used
    max_color = max(color)

    # Output the result
    print(max_color)
    print(' '.join(map(str, color)))

# Input reading
n = int(input())
s = input()

min_colors_to_sort(n, s)