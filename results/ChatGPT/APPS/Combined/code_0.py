def max_acordion_length(s: str) -> int:
    left_bracket_index = s.find('[')
    right_bracket_index = s.rfind(']')

    # Check if valid brackets are found
    if left_bracket_index == -1 or right_bracket_index == -1 or left_bracket_index >= right_bracket_index:
        return -1

    # Count colons and vertical lines between the brackets
    colon_count = s[left_bracket_index + 1:right_bracket_index].count(':')
    vertical_line_count = s[left_bracket_index + 1:right_bracket_index].count('|')

    # We need at least two colons for a valid accordion
    if colon_count < 2:
        return -1

    # The maximum length of the accordion
    return 2 + vertical_line_count  # 2 for the colons and the vertical lines in between

# Example usage
s = input().strip()
print(max_acordion_length(s))