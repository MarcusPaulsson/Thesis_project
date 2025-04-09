def min_colors_to_sort(n, s):
    color = [0] * n
    color_count = 0
    last_color = {}
    
    for i in range(n):
        char = s[i]
        if char in last_color:
            # Use the last assigned color if it can be reused
            if last_color[char] != color[i - 1]:
                color[i] = color_count + 1
                color_count += 1
            else:
                color[i] = color[i - 1]
        else:
            # Assign a new color
            color_count += 1
            color[i] = color_count
        
        last_color[char] = color[i]
    
    return color_count, color

# Input reading
n = int(input())
s = input()

# Get the result
result_count, result_colors = min_colors_to_sort(n, s)

# Output the result
print(result_count)
print(" ".join(map(str, result_colors)))