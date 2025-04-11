def max_length_accordion(s):
    n = len(s)
    left_bracket_index = -1
    right_bracket_index = -1
    max_length = -1

    # Find the first opening bracket
    for i in range(n):
        if s[i] == '[':
            left_bracket_index = i
            break

    # Find the last closing bracket
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket_index = i
            break

    # If we didn't find both brackets or they are in the wrong order, return -1
    if left_bracket_index == -1 or right_bracket_index == -1 or left_bracket_index >= right_bracket_index:
        return -1

    # Now we need to find the colons and vertical lines
    first_colon_index = -1
    second_colon_index = -1
    vertical_lines_count = 0

    # Find the first colon after the left bracket
    for i in range(left_bracket_index + 1, right_bracket_index):
        if s[i] == ':':
            if first_colon_index == -1:
                first_colon_index = i
            elif second_colon_index == -1:
                second_colon_index = i
                break
        elif s[i] == '|':
            if first_colon_index != -1:
                vertical_lines_count += 1

    # If we didn't find two colons, return -1
    if first_colon_index == -1 or second_colon_index == -1:
        return -1

    # The maximum length of the accordion
    max_length = 4 + vertical_lines_count  # 4 for [::] and vertical lines in between

    return max_length

# Read input
s = input().strip()
# Get the result and print it
print(max_length_accordion(s))