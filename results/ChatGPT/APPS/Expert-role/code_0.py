def max_acordion_length(s):
    # Initialize variables to track positions of brackets and colons
    open_bracket = -1
    first_colon = -1
    last_colon = -1
    close_bracket = -1
    
    # Iterate over the string to find positions
    for i in range(len(s)):
        if s[i] == '[' and open_bracket == -1:
            open_bracket = i
        elif s[i] == ':' and open_bracket != -1 and first_colon == -1:
            first_colon = i
        elif s[i] == ':' and first_colon != -1:
            last_colon = i
        elif s[i] == ']' and open_bracket != -1 and last_colon != -1:
            close_bracket = i
            break
    
    # Check if we have found a valid accordion structure
    if open_bracket == -1 or first_colon == -1 or last_colon == -1 or close_bracket == -1:
        return -1
    
    # Calculate the number of vertical lines
    vertical_lines = last_colon - first_colon - 1
    
    # The length of the accordion is the sum of the components
    max_length = 4 + vertical_lines
    return max_length

# Read input
s = input().strip()
# Output the result
print(max_acordion_length(s))