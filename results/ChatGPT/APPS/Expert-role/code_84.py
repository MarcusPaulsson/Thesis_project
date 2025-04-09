def can_color_string(n, s):
    # Count the occurrences of each character
    from collections import Counter
    count = Counter(s)
    
    # If any character appears more than twice, it is impossible to color
    if any(c > 2 for c in count.values()):
        return "NO"
    
    # Create a list to store the coloring
    coloring = ['0'] * n
    
    # We will use two colors: '0' and '1'
    color = 0
    
    # Last seen position for each character
    last_seen = {}
    
    for i in range(n):
        char = s[i]
        
        # If we have seen this character before, color it the same as the last one
        if char in last_seen:
            coloring[i] = coloring[last_seen[char]]
        else:
            # Assign a new color
            coloring[i] = str(color)
            color = 1 - color  # Toggle color for next unique character
            
        last_seen[char] = i
    
    return "YES", ''.join(coloring)

# Input reading
n = int(input())
s = input().strip()

# Check and output the result
result = can_color_string(n, s)
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])