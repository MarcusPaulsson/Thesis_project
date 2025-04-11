def min_colors_to_sort(n, s):
    # Step 1: Create a list to store the color assignments
    colors = [0] * n
    
    # Step 2: Create a dictionary to track the last seen index of each character
    last_seen = {}
    
    # Step 3: Initialize the color counter
    color_count = 0
    
    # Step 4: Iterate through the string
    for i in range(n):
        char = s[i]
        
        # If the character has been seen before, use the same color
        if char in last_seen:
            colors[i] = colors[last_seen[char]]
        else:
            # If it's a new character, increment the color count and assign a new color
            color_count += 1
            colors[i] = color_count
        
        # Update the last seen index for the character
        last_seen[char] = i
    
    # Step 5: Output the result
    print(color_count)
    print(' '.join(map(str, colors)))

# Example usage
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)