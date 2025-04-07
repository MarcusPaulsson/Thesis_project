def min_colors_to_sort(n, s):
    # Create a list to store the coloring
    colors = [0] * n
    color = 1
    last_seen = {}
    
    for i in range(n):
        char = s[i]
        # If this character has been seen before and is not adjacent
        if char in last_seen and last_seen[char] != i - 1:
            colors[i] = color + 1
            color += 1
        else:
            colors[i] = color
        
        last_seen[char] = i  # Update last seen position
    
    # The number of colors used
    res = max(colors)
    
    return res, colors

# Input reading
n = int(input())
s = input().strip()

# Get the result
res, coloring = min_colors_to_sort(n, s)

# Output the result
print(res)
print(" ".join(map(str, coloring)))