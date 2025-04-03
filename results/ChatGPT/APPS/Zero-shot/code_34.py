def can_color_string(n, s):
    # Count occurrences of each character
    from collections import Counter
    count = Counter(s)
    
    # Check if there are more than 2 of any character
    if any(v > 2 for v in count.values()):
        return "NO", None

    # Prepare a color array
    color = ['0'] * n
    used_colors = {}
    
    # Assign colors
    for i in range(n):
        char = s[i]
        
        if char not in used_colors:
            # If it's the first occurrence, assign color '0'
            used_colors[char] = '0'
            color[i] = '0'
        else:
            # If it's the second occurrence, assign color '1'
            if used_colors[char] == '0':
                used_colors[char] = '1'
                color[i] = '1'
            else:
                color[i] = '0'  # If it already used '1', assign '0' again

    return "YES", ''.join(color)

# Read input
n = int(input().strip())
s = input().strip()

# Get the result
result, coloring = can_color_string(n, s)

# Print the result
print(result)
if coloring is not None:
    print(coloring)