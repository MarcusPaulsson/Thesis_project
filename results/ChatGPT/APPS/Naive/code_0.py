def max_acordion_length(s):
    # Initialize variables to track the positions of the required characters
    open_bracket = -1
    first_colon = -1
    last_colon = -1
    close_bracket = -1
    
    # Iterate through the string to find the required characters
    for i, char in enumerate(s):
        if char == '[' and open_bracket == -1:
            open_bracket = i
        elif char == ':' and open_bracket != -1 and first_colon == -1:
            first_colon = i
        elif char == ':' and first_colon != -1:
            last_colon = i
        elif char == ']' and last_colon != -1 and close_bracket == -1:
            close_bracket = i
    
    # Check if we found all necessary parts of the accordion
    if open_bracket == -1 or first_colon == -1 or last_colon == -1 or close_bracket == -1:
        return -1
    
    # Calculate the maximum length of the accordion
    vertical_lines = last_colon - first_colon - 1
    max_length = 4 + vertical_lines  # 4 for the brackets and colons
    
    return max_length

# Read input
s = input().strip()
# Output the result
print(max_acordion_length(s))