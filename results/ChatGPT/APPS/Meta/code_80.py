def min_colors_to_sort_string(n, s):
    # Dictionary to store the last seen index of each character
    last_seen = {}
    # List to store the color assignments
    colors = [0] * n
    # The color counter
    color_count = 0

    for i in range(n):
        char = s[i]
        if char in last_seen:
            # If current character was seen before, assign the same color
            colors[i] = colors[last_seen[char]]
        else:
            # If it's a new character, increment color count and assign new color
            color_count += 1
            colors[i] = color_count
            
        # Update the last seen index of the character
        last_seen[char] = i

    return color_count, colors

# Read input
n = int(input())
s = input()

# Get the result
res, coloring = min_colors_to_sort_string(n, s)

# Print the results
print(res)
print(' '.join(map(str, coloring)))