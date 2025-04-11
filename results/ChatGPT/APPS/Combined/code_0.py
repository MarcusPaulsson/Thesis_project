def max_acordion_length(s: str) -> int:
    left_bracket_index = s.find('[')
    colon_index = s.find(':', left_bracket_index + 1)
    right_bracket_index = s.rfind(']', colon_index + 1)
    
    if left_bracket_index == -1 or colon_index == -1 or right_bracket_index == -1:
        return -1

    vertical_lines_count = s.count('|', colon_index + 1, right_bracket_index)

    # Calculate the maximum length of the accordion
    accordion_length = 2 + vertical_lines_count  # 2 for the brackets and colons
    return accordion_length

# Example usage
s = input().strip()
print(max_acordion_length(s))