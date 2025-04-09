def max_acordion_length(s):
    # Initialize variables to find the first and last brackets and colons
    left_bracket_index = -1
    right_bracket_index = -1
    first_colon_index = -1
    last_colon_index = -1
    
    # Iterate through the string to find required characters
    for i, char in enumerate(s):
        if char == '[' and left_bracket_index == -1:
            left_bracket_index = i
        elif char == ']' and left_bracket_index != -1:
            right_bracket_index = i
        elif char == ':' and first_colon_index == -1:
            first_colon_index = i
        elif char == ':':
            last_colon_index = i
    
    # Check if we found valid indices for accordion structure
    if left_bracket_index == -1 or right_bracket_index == -1 or first_colon_index == -1 or last_colon_index == -1:
        return -1
    
    # Ensure that the colons are correctly positioned
    if first_colon_index >= last_colon_index or left_bracket_index >= first_colon_index or right_bracket_index <= last_colon_index:
        return -1
    
    # Count the number of '|' characters between the colons
    vertical_lines_count = s[first_colon_index + 1:last_colon_index].count('|')
    
    # Calculate the maximum length of the accordion
    return 4 + vertical_lines_count  # 4 for the brackets and colons, plus the number of '|'

# Input reading
s = input().strip()
# Output the result
print(max_acordion_length(s))