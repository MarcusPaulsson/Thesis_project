def max_length Accordion(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1

    # Find the last opening bracket '['
    for i in range(n):
        if s[i] == '[':
            left_bracket = i

    # Find the first closing bracket ']'
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket = i

    # If there are no valid brackets, return -1
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1

    # Find the first colon after the left bracket
    first_colon = -1
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == ':':
            first_colon = i
            break

    # If no colon found, return -1
    if first_colon == -1:
        return -1

    # Find the last colon before the right bracket
    last_colon = -1
    for i in range(right_bracket - 1, left_bracket, -1):
        if s[i] == ':':
            last_colon = i
            break

    # If no colon found, return -1
    if last_colon == -1 or last_colon <= first_colon:
        return -1

    # Count the number of vertical lines between the two colons
    vertical_lines = 0
    for i in range(first_colon + 1, last_colon):
        if s[i] == '|':
            vertical_lines += 1

    # Maximum length of the accordion
    return 4 + vertical_lines

# Input
s = input().strip()
# Output
print(max_length Accordion(s))