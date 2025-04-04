def minimum_colors_to_sort(n, s):
    from collections import defaultdict

    last_position = {}
    colors = [0] * n
    color_count = 0

    # Step 1: Determine the last position of each character
    for i in range(n):
        last_position[s[i]] = i

    # Step 2: Assign colors based on the last known position of characters
    for i in range(n):
        if i == 0:
            color_count += 1
            colors[i] = color_count
        else:
            # If the current character is the same as the previous one, keep the same color
            if s[i] == s[i - 1]:
                colors[i] = colors[i - 1]
            else:
                # If we encounter a new character, we need to check the last position
                if last_position[s[i - 1]] < i:
                    color_count += 1
                colors[i] = color_count

    return color_count, colors

# Input reading
n = int(input().strip())
s = input().strip()

# Get the result
res, coloring = minimum_colors_to_sort(n, s)

# Output the result
print(res)
print(' '.join(map(str, coloring)))