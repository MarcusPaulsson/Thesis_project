def max_accordion_length(s):
    # Initialize variables to track positions of brackets and colons
    left_bracket = -1
    right_bracket = -1
    first_colon = -1
    last_colon = -1
    
    # Find the first opening bracket
    for i in range(len(s)):
        if s[i] == '[':
            left_bracket = i
            break
            
    # Find the last closing bracket
    for i in range(len(s)-1, -1, -1):
        if s[i] == ']':
            right_bracket = i
            break
            
    # If no brackets found or brackets are in the wrong order
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1
    
    # Find the first colon after the opening bracket
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == ':':
            first_colon = i
            break
            
    # Find the last colon before the closing bracket
    for i in range(right_bracket - 1, left_bracket, -1):
        if s[i] == ':':
            last_colon = i
            break
            
    # If no colons found or they are in the wrong order
    if first_colon == -1 or last_colon == -1 or first_colon >= last_colon:
        return -1
    
    # Count vertical lines between the first and last colons
    vertical_lines_count = 0
    for i in range(first_colon + 1, last_colon):
        if s[i] == '|':
            vertical_lines_count += 1
            
    # The maximum length of the accordion
    return 4 + vertical_lines_count  # 4 for the brackets and colons

# Input
s = input().strip()
# Output
print(max_accordion_length(s))