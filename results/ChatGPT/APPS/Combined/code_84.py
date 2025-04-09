def can_color_string(n, s):
    # Initialize a list to hold the color assignment
    color = ['0'] * n
    last_positions = {}

    # Track last positions of each character
    for i in range(n):
        char = s[i]
        if char in last_positions:
            last_positions[char].append(i)
        else:
            last_positions[char] = [i]

    # Check the possibility to color the string
    for positions in last_positions.values():
        for i in range(1, len(positions)):
            if positions[i] - positions[i - 1] == 1:
                continue
            if color[positions[i]] == color[positions[i - 1]]:
                return "NO", ""

    # Color the string based on sorted order
    color_map = {}
    for i in range(n):
        char = s[i]
        if char not in color_map:
            color_map[char] = '0' if len(color_map) % 2 == 0 else '1'
        color[i] = color_map[char]
    
    return "YES", ''.join(color)

# Input handling
n = int(input())
s = input().strip()

# Get the result
result, coloring = can_color_string(n, s)

# Output the result
print(result)
if result == "YES":
    print(coloring)