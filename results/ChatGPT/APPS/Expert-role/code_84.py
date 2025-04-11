def can_color_string(n, s):
    # Count occurrences of each character
    from collections import Counter
    count = Counter(s)
    
    # Check if any character appears more than twice
    if any(c > 2 for c in count.values()):
        return "NO"
    
    # Prepare the coloring
    color = ['0'] * n
    last_color = '0'
    
    # Assign colors
    for i in range(n):
        if i > 0 and s[i] == s[i - 1]:
            color[i] = last_color
        else:
            last_color = '1' if last_color == '0' else '0'
            color[i] = last_color
    
    return "YES", ''.join(color)

# Input reading
n = int(input())
s = input().strip()

# Get the result
result = can_color_string(n, s)

# Output the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])