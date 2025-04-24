def can_color_string(n, s):
    from collections import Counter
    
    # Count occurrences of each character
    count = Counter(s)
    
    # Check if any character appears more than twice
    if any(v > 2 for v in count.values()):
        return "NO"
    
    # Prepare the coloring array
    coloring = ['0'] * n
    last_color = '0'
    
    # Assign colors based on the characters
    for i in range(n):
        if i > 0 and s[i] == s[i - 1]:
            coloring[i] = last_color
        else:
            last_color = '1' if last_color == '0' else '0'
            coloring[i] = last_color
    
    return "YES\n" + ''.join(coloring)

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(can_color_string(n, s))