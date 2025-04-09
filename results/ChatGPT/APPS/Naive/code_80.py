def min_colors_to_sort(n, s):
    color_count = 1
    colors = [0] * n
    last_position = {}

    for i in range(n):
        char = s[i]
        if char in last_position:
            # If the character was seen before, check if we need a new color
            if last_position[char] != -1:
                for j in range(last_position[char] + 1, i):
                    if s[j] < char and colors[j] == 0:
                        # If we find a character that is less than the current character
                        # and is not yet colored, we need a new color
                        color_count += 1
                        break
                colors[i] = color_count
            else:
                colors[i] = colors[last_position[char]]
        else:
            colors[i] = color_count
        
        last_position[char] = i

    # Assign colors based on the previous assignments
    for i in range(n):
        if colors[i] == 0:
            colors[i] = color_count

    return color_count, colors

# Read input
n = int(input())
s = input().strip()

# Get the result
res, coloring = min_colors_to_sort(n, s)

# Print output
print(res)
print(' '.join(map(str, coloring)))