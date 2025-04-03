def can_color_string(n, s):
    # Create a list to store the positions of each character
    positions = {}
    
    for i, char in enumerate(s):
        if char not in positions:
            positions[char] = []
        positions[char].append(i)
    
    # Prepare to create the coloring
    color = [''] * n
    current_color = 0
    
    # Sort the keys to iterate in alphabetical order
    sorted_chars = sorted(positions.keys())
    
    for char in sorted_chars:
        # Get the indices for this character
        indices = positions[char]
        
        # Check if we can color without conflict
        for index in indices:
            if color[index] == '':
                color[index] = str(current_color)
            else:
                # Conflict in coloring
                if color[index] != str(current_color):
                    return "NO"
        
        # Switch color for the next character
        current_color = 1 - current_color
    
    return "YES", ''.join(color)

# Read input
n = int(input().strip())
s = input().strip()

# Get the result
result = can_color_string(n, s)

# Print the output
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])