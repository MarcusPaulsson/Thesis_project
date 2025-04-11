def max_acordion_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    colon_count = 0
    vertical_lines = 0

    # Find the first opening bracket
    for i in range(n):
        if s[i] == '[':
            left_bracket = i
            break

    # If no opening bracket found
    if left_bracket == -1:
        return -1

    # Find the last closing bracket
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket = i
            break

    # If no closing bracket found
    if right_bracket == -1 or right_bracket <= left_bracket:
        return -1

    # Count colons and vertical lines between the brackets
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == ':':
            colon_count += 1
        elif s[i] == '|':
            vertical_lines += 1

    # We need exactly 2 colons for a valid accordion
    if colon_count < 2:
        return -1

    # The maximum length of the accordion
    return 4 + vertical_lines  # 4 for [::] + vertical lines

# Read input
s = input().strip()
# Output the result
print(max_acordion_length(s))