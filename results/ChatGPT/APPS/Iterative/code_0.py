s = input().strip()

# Initialize variables to track the positions of brackets and colons
open_bracket_index = s.find('[')
first_colon_index = s.find(':', open_bracket_index)
last_colon_index = s.rfind(':', first_colon_index)
close_bracket_index = s.find(']', last_colon_index)

# Determine if a valid accordion can be formed
if open_bracket_index != -1 and first_colon_index != -1 and last_colon_index != -1 and close_bracket_index != -1:
    # Calculate the maximum length of the accordion
    vertical_lines_count = s[first_colon_index + 1:last_colon_index].count('|')
    max_length = 5 + vertical_lines_count  # [ : |* : ]
    print(max_length)
else:
    print(-1)