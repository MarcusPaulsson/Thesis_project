def min_colors_to_sort(n, s):
    colors = [0] * n
    color_count = 0
    last_seen = {}
    
    for i in range(n):
        char = s[i]
        if char in last_seen:
            colors[i] = last_seen[char]
        else:
            color_count += 1
            last_seen[char] = color_count
            colors[i] = color_count
            
        # Ensure that we maintain the correct colorings for sorting
        for j in range(i):
            if s[j] > s[i] and colors[j] == colors[i]:
                colors[j] = color_count + 1
                color_count += 1
                
    print(color_count)
    print(' '.join(map(str, colors)))

# Read input
n = int(input().strip())
s = input().strip()

min_colors_to_sort(n, s)