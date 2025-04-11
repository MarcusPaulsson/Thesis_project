def min_colors_to_sort(n, s):
    from collections import defaultdict
    
    # Create a mapping of character positions
    char_positions = defaultdict(list)
    for index, char in enumerate(s):
        char_positions[char].append(index)
    
    # Create a list to store the color for each character
    colors = [0] * n
    current_color = 1
    
    # Iterate through the sorted unique characters
    sorted_chars = sorted(char_positions.keys())
    
    # Assign colors based on the positions of characters
    for char in sorted_chars:
        positions = char_positions[char]
        for i in range(len(positions)):
            colors[positions[i]] = (i % current_color) + 1
        current_color = max(current_color, len(positions))
    
    # The number of colors used
    res = max(colors)
    
    print(res)
    print(" ".join(map(str, colors)))

# Example usage
n = int(input())
s = input().strip()
min_colors_to_sort(n, s)