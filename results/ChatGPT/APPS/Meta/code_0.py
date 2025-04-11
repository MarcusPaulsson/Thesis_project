def max_length_accordion(s):
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
            
    # Check if we have found all necessary components for an accordion
    if left_bracket == -1 or first_colon == -1 or last_colon == -1 or right_bracket == -1:
        return -1
    
    # Calculate the maximum length of the accordion
    # The length is determined by the positions of the brackets and colons
    max_length = right_bracket - left_bracket + 1
    return max_length

# Example usage
s = input().strip()
print(max_length_accordion(s))