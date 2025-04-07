def max_accordion_length(s):
    # Initialize positions for the required characters
    left_bracket_pos = s.find('[')
    first_colon_pos = s.find(':', left_bracket_pos + 1)
    second_colon_pos = s.find(':', first_colon_pos + 1)
    right_bracket_pos = s.find(']', second_colon_pos + 1)

    # Check if all required characters were found in the correct order
    if left_bracket_pos == -1 or first_colon_pos == -1 or second_colon_pos == -1 or right_bracket_pos == -1:
        return -1

    # Calculate the number of vertical lines '|' between the two colons
    vertical_lines_count = s[first_colon_pos + 1:second_colon_pos].count('|')

    # The length of the accordion is 4 (for the brackets and colons) plus the vertical lines
    return 4 + vertical_lines_count

# Input reading
s = input().strip()
# Output the maximum accordion length
print(max_accordion_length(s))