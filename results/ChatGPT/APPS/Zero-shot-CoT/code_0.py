def max_accordion_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    
    # Find the first opening bracket '['
    for i in range(n):
        if s[i] == '[':
            left_bracket = i
            break
            
    # Find the last closing bracket ']'
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket = i
            break
            
    # If we don't have both brackets, return -1
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1
    
    # Now we need to find the colons ':' and vertical lines '|'
    first_colon = -1
    second_colon = -1
    vertical_lines_count = 0
    
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == ':':
            if first_colon == -1:
                first_colon = i
            elif second_colon == -1:
                second_colon = i
                break
        elif s[i] == '|':
            vertical_lines_count += 1
            
    # If we don't have two colons, return -1
    if first_colon == -1 or second_colon == -1:
        return -1
    
    # Calculate the maximum length of the accordion
    max_length = 2 + vertical_lines_count  # 2 for the colons and brackets
    return max_length + 2  # +2 for the brackets

# Read input
s = input().strip()
# Get the result
result = max_accordion_length(s)
# Print the result
print(result)