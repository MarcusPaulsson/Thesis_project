def max_accordion_length(s):
    left_bracket_index = s.find('[')
    right_bracket_index = s.rfind(']')
    
    if left_bracket_index == -1 or right_bracket_index == -1 or right_bracket_index < left_bracket_index:
        return -1

    colon_count = s.count(':', left_bracket_index, right_bracket_index)
    
    if colon_count < 2:
        return -1

    vertical_lines = s.count('|', left_bracket_index, right_bracket_index)
    
    max_length = 4 + vertical_lines
    return max_length

# Read input
s = input().strip()
# Output the result
print(max_accordion_length(s))