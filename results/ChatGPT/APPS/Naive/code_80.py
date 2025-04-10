def min_colors_to_sort(n, s):
    # Create a list to store the color assignments
    colors = [0] * n
    # Dictionary to track the last seen index of each character
    last_seen = {}
    # Color counter
    color_count = 0

    for i in range(n):
        char = s[i]
        if char in last_seen:
            # If the character was seen before, assign the same color
            colors[i] = colors[last_seen[char]]
        else:
            # If it's a new character, increment the color count and assign a new color
            color_count += 1
            colors[i] = color_count
        
        # Update the last seen index for the character
        last_seen[char] = i

    return color_count, colors

# Input reading
n = int(input())
s = input().strip()

# Get the result
result_count, result_colors = min_colors_to_sort(n, s)

# Output the results
print(result_count)
print(' '.join(map(str, result_colors)))