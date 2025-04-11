def max_accordion_length(s):
    # Find the first occurrence of '[' and the last occurrence of ']'
    open_bracket_index = s.find('[')
    close_bracket_index = s.rfind(']')
    
    # If both brackets are found and in the correct order
    if open_bracket_index != -1 and close_bracket_index != -1 and open_bracket_index < close_bracket_index:
        # Find the first occurrence of ':' after the opening bracket
        first_colon_index = s.find(':', open_bracket_index + 1)
        
        # Find the last occurrence of ':' before the closing bracket
        last_colon_index = s.rfind(':', close_bracket_index - 1)
        
        # If both colons are found and in the correct order
        if first_colon_index != -1 and last_colon_index != -1 and first_colon_index < last_colon_index:
            # Calculate the number of '|' characters between the two colons
            pipe_count = s.count('|', first_colon_index + 1, last_colon_index)
            
            # The length of the accordion is the sum of the positions of the closing and opening brackets
            # plus the number of '|' characters plus 2 for the colons
            return close_bracket_index - open_bracket_index + pipe_count + 2
        else:
            return -1
    else:
        return -1

# Read input string
s = input().strip()

# Print the maximum possible length of the resulting accordion
print(max_accordion_length(s))