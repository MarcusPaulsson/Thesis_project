n = int(input())
s = input()

# Create a list to store colors for each character in the string
colors = [0] * n
color_count = 0

# A dictionary to track the last used color for each character
last_color = {}

# Iterate through the string and assign colors
for i in range(n):
    char = s[i]
    # If the character has been seen before, use the last assigned color
    if char in last_color:
        colors[i] = last_color[char]
    else:
        # Assign a new color
        color_count += 1
        last_color[char] = color_count
        colors[i] = color_count

# Output the results
print(color_count)
print(' '.join(map(str, colors)))