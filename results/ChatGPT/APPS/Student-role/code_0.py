def max_acc_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    colon_count = 0
    pipe_count = 0

    # Find the first opening bracket
    for i in range(n):
        if s[i] == '[':
            left_bracket = i
            break

    # Find the last closing bracket
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket = i
            break

    # If we don't have both brackets
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1

    # Count colons and pipes between the brackets
    for i in range(left_bracket, right_bracket + 1):
        if s[i] == ':':
            colon_count += 1
        elif s[i] == '|':
            pipe_count += 1

    # We need at least two colons to form an accordion
    if colon_count < 2:
        return -1

    # The maximum length of the accordion
    return 2 + pipe_count  # 2 for the colons, plus the number of pipes

# Read input
s = input().strip()
# Output the result
print(max_acc_length(s))