def max_accordion_length(s):
    left_bracket_index = -1
    right_bracket_index = -1
    colon_indices = []

    for i, char in enumerate(s):
        if char == '[' and left_bracket_index == -1:
            left_bracket_index = i
        elif char == ':' and left_bracket_index != -1:
            colon_indices.append(i)
        elif char == ']' and left_bracket_index != -1:
            right_bracket_index = i
            break

    if left_bracket_index == -1 or right_bracket_index == -1 or len(colon_indices) < 2:
        return -1

    # We need at least two colons, one before the vertical lines and one after
    # We will find the first colon after the left bracket and the last colon before the right bracket
    first_colon_index = -1
    last_colon_index = -1

    for i in colon_indices:
        if i > left_bracket_index:
            if first_colon_index == -1:
                first_colon_index = i
            if i < right_bracket_index:
                last_colon_index = i

    if first_colon_index == -1 or last_colon_index == -1 or first_colon_index >= last_colon_index:
        return -1

    # Count the vertical lines between the two colons
    vertical_lines_count = 0
    for i in range(first_colon_index + 1, last_colon_index):
        if s[i] == '|':
            vertical_lines_count += 1

    # Length of accordion = 1 (for [) + 1 (for :) + vertical lines + 1 (for :) + 1 (for ])
    return 4 + vertical_lines_count

# Read input
s = input().strip()
# Get the result and print it
print(max_accordion_length(s))