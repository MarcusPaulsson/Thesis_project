def can_color_string(n, s):
    # Count the occurrences of each character
    from collections import Counter
    count = Counter(s)
    
    # Check if any character appears more than twice
    if any(v > 2 for v in count.values()):
        return "NO"
    
    # Initialize the coloring array
    coloring = ['0'] * n
    
    # We will use two colors: '0' and '1'
    color = 0
    
    # Assign colors based on the character's position
    for i in range(n):
        if i > 0 and s[i] == s[i - 1]:
            coloring[i] = coloring[i - 1]  # Same color as previous
        else:
            coloring[i] = str(color)  # Alternate colors
            color = 1 - color  # Switch color
    
    return "YES", ''.join(coloring)

# Read input
n = int(input().strip())
s = input().strip()

# Get the result
result = can_color_string(n, s)

# Print the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])