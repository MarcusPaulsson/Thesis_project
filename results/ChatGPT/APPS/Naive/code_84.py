def can_color_string(n, s):
    color = ['0'] * n  # Initialize all characters with color '0'
    
    # Create a sorted version of the string
    sorted_s = sorted(s)
    
    # Map to keep track of the count of each character
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    # Create a position marker for when we should switch colors
    position = 0
    for char in sorted(count.keys()):
        current_count = count[char]
        # We assign color '0' to the first half and '1' to the second half
        for i in range(position, position + current_count):
            if i < n // 2:
                color[i] = '0'
            else:
                color[i] = '1'
        position += current_count
    
    # Check if the resulting coloring can actually sort the string
    # by comparing the original and the colored version
    colored_s = ''.join(color)
    for i in range(1, n):
        if s[i] < s[i - 1] and colored_s[i] == colored_s[i - 1]:
            return "NO"
    
    return "YES\n" + ''.join(color)

# Input reading
n = int(input())
s = input().strip()

# Get the result
result = can_color_string(n, s)

# Print the result
print(result)