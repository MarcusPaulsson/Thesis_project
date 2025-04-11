def max_acordion_length(s):
    # Initialize variables to track the positions of the required characters
    left_bracket = -1
    first_colon = -1
    last_colon = -1
    right_bracket = -1
    
    # Iterate through the string to find the required characters
    for i, char in enumerate(s):
        if char == '[' and left_bracket == -1:
            left_bracket = i
        elif char == ':' and left_bracket != -1 and first_colon == -1:
            first_colon = i
        elif char == ':' and first_colon != -1:
            last_colon = i
        elif char == ']' and last_colon != -1 and right_bracket == -1:
            right_bracket = i
            
    # Check if we found a valid accordion structure
    if left_bracket == -1 or first_colon == -1 or last_colon == -1 or right_bracket == -1:
        return -1
    
    # Calculate the maximum length of the accordion
    vertical_lines_count = last_colon - first_colon - 1
    accordion_length = 4 + vertical_lines_count  # 4 for [::]
    
    return accordion_length

# Read input
s = input().strip()
# Output the result
print(max_acordion_length(s))