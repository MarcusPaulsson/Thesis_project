def can_color_string(n, s):
    from collections import Counter
    
    # Count occurrences of each character
    count = Counter(s)
    
    # Check if any character appears more than twice
    if any(cnt > 2 for cnt in count.values()):
        return "NO", ""
    
    # Create a coloring scheme
    color = ['0'] * n
    last_color = '0'
    
    for i in range(n):
        if i > 0 and s[i] == s[i - 1]:
            color[i] = color[i - 1]  # Same color as previous
        else:
            # Alternate color
            last_color = '1' if last_color == '0' else '0'
            color[i] = last_color
    
    return "YES", ''.join(color)

# Input reading
n = int(input())
s = input().strip()

# Get the result
result, coloring = can_color_string(n, s)

# Output the result
print(result)
if result == "YES":
    print(coloring)