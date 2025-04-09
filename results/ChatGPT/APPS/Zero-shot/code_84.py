def can_color_sort(s):
    n = len(s)
    color = [''] * n
    last_seen = {}
    
    for i in range(n):
        char = s[i]
        if char in last_seen:
            if last_seen[char] == '0':
                color[i] = '1'
            else:
                color[i] = '0'
        else:
            color[i] = '0' if i % 2 == 0 else '1'
        
        last_seen[char] = color[i]
    
    for i in range(n - 1):
        if s[i] > s[i + 1] and color[i] == color[i + 1]:
            return "NO"
    
    return "YES", ''.join(color)

# Input reading
n = int(input().strip())
s = input().strip()

# Check if possible to color and sort
result = can_color_sort(s)
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])