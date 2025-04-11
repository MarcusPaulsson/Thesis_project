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
            
    # Check if we found a valid accordion structure
    if open_bracket == -1 or first_colon == -1 or last_colon == -1 or close_bracket == -1:
        return -1
    
    # Calculate the number of vertical lines between the colons
    vertical_lines_count = last_colon - first_colon - 1
    
    # Calculate the total length of the accordion
    accordion_length = 4 + vertical_lines_count
    
    return accordion_length

# Read input
s = input().strip()
# Get the maximum accordion length
result = max_acordion_length(s)
# Print the result
print(result)