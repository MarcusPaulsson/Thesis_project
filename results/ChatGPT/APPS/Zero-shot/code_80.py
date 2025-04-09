def min_colors_to_sort(n, s):
    from collections import defaultdict
    
    # Step 1: Find the positions of each character
    positions = defaultdict(list)
    for i, char in enumerate(s):
        positions[char].append(i)
    
    # Step 2: Determine the minimum number of colors needed
    color = [0] * n
    next_color = 1
    last_used = [-1] * 26  # Track the last color used for each character
    
    for i, char in enumerate(s):
        index = ord(char) - ord('a')
        if last_used[index] == -1:
            # If this character has not been colored yet
            color[i] = next_color
            last_used[index] = next_color
            next_color += 1
        else:
            # If this character has been colored, use the same color
            color[i] = last_used[index]

    # Output the result
    print(next_color - 1)
    print(' '.join(map(str, color)))

# Example input
n = int(input().strip())
s = input().strip()
min_colors_to_sort(n, s)