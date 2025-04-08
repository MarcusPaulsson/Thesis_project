def can_color_string(n, s):
    # Create a list to represent the coloring
    coloring = ['0'] * n
    
    # Dictionary to count occurrences of each character
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check if any character appears more than 2 times
    if any(count > 2 for count in char_count.values()):
        return "NO"
    
    # Assign colors based on character positions
    color_toggle = {}
    for i in range(n):
        char = s[i]
        if char not in color_toggle:
            color_toggle[char] = 0  # Start with color '0'
        coloring[i] = str(color_toggle[char])
        # Toggle the color for the next occurrence of the same character
        color_toggle[char] = 1 - color_toggle[char]
    
    return "YES", ''.join(coloring)

# Read input
n = int(input().strip())
s = input().strip()

# Get the result
result = can_color_string(n, s)

# Print output
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])