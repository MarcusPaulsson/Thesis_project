def max_acc_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    
    # Find the last opening bracket
    for i in range(n):
        if s[i] == '[':
            left_bracket = i
    
    # Find the first closing bracket
    for i in range(n-1, -1, -1):
        if s[i] == ']':
            right_bracket = i
            
    # If we don't have both brackets, return -1
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1
    
    # Now look for colons and vertical lines
    first_colon = -1
    second_colon = -1
    
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == ':':
            if first_colon == -1:
                first_colon = i
            elif second_colon == -1:
                second_colon = i
                break
    
    # If we don't have two colons, return -1
    if first_colon == -1 or second_colon == -1:
        return -1
    
    # Determine the number of vertical lines between the colons
    vertical_lines = second_colon - first_colon - 1
    
    # The length of the accordion is the fixed part plus vertical lines
    accordion_length = 4 + vertical_lines
    
    return accordion_length

# Read input
s = input().strip()
# Get result and print
result = max_acc_length(s)
print(result)