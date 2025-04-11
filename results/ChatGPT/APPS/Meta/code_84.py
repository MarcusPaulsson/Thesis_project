def can_color_string(n, s):
    # Create a list to store the color of each character
    color = [''] * n
    
    # Create a dictionary to count occurrences of each character
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Create a sorted version of the string
    sorted_s = sorted(s)
    
    # Check if we can color the string
    for i in range(n):
        if s[i] != sorted_s[i]:
            # If the current character is not in the same position as in sorted string
            # we need to color it differently
            if color[i] == '':
                # Assign color '0' to the first occurrence
                color[i] = '0'
            else:
                # If already colored, we need to assign the opposite color
                color[i] = '1' if color[i] == '0' else '0'
        else:
            # If the character is in the same position, we can color it the same
            color[i] = '0'
    
    # Check for conflicts in coloring
    for i in range(1, n):
        if s[i] < s[i - 1] and color[i] == color[i - 1]:
            return "NO"
    
    return "YES", ''.join(color)

# Read input
n = int(input())
s = input().strip()

# Get the result
result = can_color_string(n, s)

# Print the result
if result == "NO":
    print(result)
else:
    print(result[0])
    print(result[1])