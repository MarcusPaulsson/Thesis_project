def min_colors_to_sort(n, s):
    # Create a list to hold the color of each character
    color = [0] * n
    
    # A list to track the last occurrence of each character
    last_occurrence = {}
    
    # The number of colors used
    color_count = 0
    
    for i in range(n):
        char = s[i]
        
        # If character has not been seen before, use a new color
        if char not in last_occurrence:
            color_count += 1
            color[i] = color_count
        else:
            # If it has been seen, we can assign the same color
            color[i] = color[last_occurrence[char]]
        
        # Update the last occurrence of the character
        last_occurrence[char] = i
    
    return color_count, color

# Read input
n = int(input())
s = input().strip()

# Get the result
res, coloring = min_colors_to_sort(n, s)

# Print output
print(res)
print(' '.join(map(str, coloring)))