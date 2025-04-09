def max_acordion_length(s):
    # Initialize variables to track positions of key characters
    open_bracket = -1
    first_colon = -1
    last_colon = -1
    close_bracket = -1
    
    # Scan the string to find the positions of the required characters
    for i, char in enumerate(s):
        if char == '[' and open_bracket == -1:
            open_bracket = i
        elif char == ':' and open_bracket != -1 and first_colon == -1:
            first_colon = i
        elif char == ':' and first_colon != -1:
            last_colon = i
        elif char == ']' and last_colon != -1 and close_bracket == -1:
            close_bracket = i
            
    # If we didn't find all required parts for an accordion, return -1
    if open_bracket == -1 or first_colon == -1 or last_colon == -1 or close_bracket == -1:
        return -1
    
    # Count vertical lines between the first and last colon
    vertical_lines = s[first_colon + 1:last_colon].count('|')
    
    # Calculate the maximum length of the accordion
    accordion_length = 4 + vertical_lines
    
    return accordion_length

# Read input
s = input().strip()
# Print the result
print(max_acordion_length(s))