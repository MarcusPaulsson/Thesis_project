def maxAccordionLength(s: str) -> int:
    opening_bracket_index = s.find('[')
    closing_bracket_index = s.rfind(']')
    
    # Check for valid brackets
    if opening_bracket_index == -1 or closing_bracket_index == -1 or opening_bracket_index >= closing_bracket_index:
        return -1
    
    # Find the first colon after the opening bracket
    first_colon_index = s.find(':', opening_bracket_index)
    # Find the last colon before the closing bracket
    last_colon_index = s.rfind(':', opening_bracket_index, closing_bracket_index)
    
    # Check for valid colons
    if first_colon_index == -1 or last_colon_index == -1 or first_colon_index >= last_colon_index:
        return -1
    
    # Count vertical lines between the two colons
    vertical_lines_count = s[first_colon_index + 1:last_colon_index].count('|')
    
    # Calculate the maximum length of the accordion
    max_length = 4 + vertical_lines_count
    
    return max_length

# Input reading
s = input().strip()
print(maxAccordionLength(s))