def can_color_string(n, s):
    # Count occurrences of each character
    from collections import Counter
    count = Counter(s)
    
    # Check if any character appears more than twice
    for char, cnt in count.items():
        if cnt > 2:
            return "NO"
    
    # Initialize coloring
    color = ['0'] * n
    
    # Assign colors
    for i in range(n):
        if s[i] in s[:i]:
            color[i] = '1'
    
    return "YES\n" + ''.join(color)

# Input reading
n = int(input())
s = input().strip()

# Output the result
print(can_color_string(n, s))