def can_color_string(n, s):
    sorted_s = sorted(s)
    color = ['0'] * n
    
    # Create a mapping of characters to their positions in the sorted string
    char_positions = {}
    for i, char in enumerate(sorted_s):
        if char not in char_positions:
            char_positions[char] = []
        char_positions[char].append(i)
    
    # Assign colors based on the positions in the original string
    current_color = 0
    for char in s:
        if char_positions[char]:
            pos = char_positions[char].pop(0)
            color[pos] = str(current_color)
            current_color = 1 - current_color  # Alternate colors
    
    # Check if the coloring allows sorting
    for i in range(n - 1):
        if s[i] > s[i + 1] and color[i] == color[i + 1]:
            return "NO"
    
    return "YES", ''.join(color)

n = int(input())
s = input().strip()
result = can_color_string(n, s)
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])