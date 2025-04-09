def max_acc_length(s):
    n = len(s)
    l_bracket = -1
    r_bracket = -1

    # Find the last opening bracket '['
    for i in range(n):
        if s[i] == '[':
            l_bracket = i

    # Find the first closing bracket ']'
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            r_bracket = i

    # Check for valid brackets
    if l_bracket == -1 or r_bracket == -1 or l_bracket >= r_bracket:
        return -1

    # Find the first ':' after the opening bracket
    first_colon = s.find(':', l_bracket + 1, r_bracket)
    if first_colon == -1:
        return -1

    # Find the last ':' before the closing bracket
    second_colon = s.rfind(':', l_bracket, r_bracket)
    if second_colon == -1 or second_colon <= first_colon:
        return -1

    # Count the number of '|' between the colons
    vertical_lines_count = s.count('|', first_colon + 1, second_colon)

    # Calculate the length of the accordion
    accordion_length = 4 + vertical_lines_count
    return accordion_length


# Input
s = input().strip()
# Output
print(max_acc_length(s))