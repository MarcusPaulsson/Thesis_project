def min_colors_to_sort(n, s):
    # Create a list to store the color of each character
    colors = [0] * n
    # Create a dictionary to track the last seen index of each character
    last_seen = {}
    color_count = 0
    
    for i in range(n):
        char = s[i]
        if char not in last_seen:
            color_count += 1
            last_seen[char] = color_count
        colors[i] = last_seen[char]
    
    # Output the result
    print(color_count)
    print(' '.join(map(str, colors)))

# Input reading
n = int(input().strip())
s = input().strip()
min_colors_to_sort(n, s)