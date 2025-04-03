def min_colors_to_sort(n, s):
    # To hold the color assignments
    colors = [0] * n
    
    # To track the last index of each character
    last_index = {}
    
    # Assign initial colors based on the last occurrence of each character
    for i in range(n):
        char = s[i]
        if char not in last_index:
            last_index[char] = []
        last_index[char].append(i)
    
    # The maximum number of colors needed
    max_colors = 1
    
    # Now we will assign colors based on the segments of characters
    for indices in last_index.values():
        # If there are multiple indices for the same character
        for j in range(len(indices)):
            if j == 0:
                colors[indices[j]] = max_colors
            else:
                # Check if we need a new color
                if indices[j] > indices[j - 1] + 1:
                    max_colors += 1
                colors[indices[j]] = max_colors
    
    return max_colors, colors

# Read input
n = int(input())
s = input()

# Get the result
res, color_assignment = min_colors_to_sort(n, s)

# Print output
print(res)
print(" ".join(map(str, color_assignment)))