def max_accordion_length(s):
    n = len(s)
    left_bracket_index = -1
    right_bracket_index = -1

    for i in range(n):
        if s[i] == '[':
            left_bracket_index = i
        elif s[i] == ']':
            right_bracket_index = i
    
    if left_bracket_index == -1 or right_bracket_index == -1 or left_bracket_index >= right_bracket_index:
        return -1

    colon_index_left = -1
    colon_index_right = -1

    for i in range(left_bracket_index + 1, right_bracket_index):
        if s[i] == ':':
            if colon_index_left == -1:
                colon_index_left = i
            colon_index_right = i
    
    if colon_index_left == -1 or colon_index_right == -1 or colon_index_left == colon_index_right:
        return -1

    vertical_lines_count = sum(1 for i in range(colon_index_left + 1, colon_index_right) if s[i] == '|')

    return 4 + vertical_lines_count  # 4 for the fixed characters in the accordion

# Read input
s = input().strip()
# Output the result
print(max_accordion_length(s))