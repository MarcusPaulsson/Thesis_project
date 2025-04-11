def max_length_accordion(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    colon_count = 0
    vertical_count = 0

    for i in range(n):
        if s[i] == '[':
            left_bracket = i
        elif s[i] == ']':
            right_bracket = i
            if left_bracket != -1 and right_bracket > left_bracket:
                # Count colons and vertical lines between the brackets
                for j in range(left_bracket + 1, right_bracket):
                    if s[j] == ':':
                        colon_count += 1
                    elif s[j] == '|':
                        vertical_count += 1

    if left_bracket == -1 or right_bracket == -1 or colon_count < 2:
        return -1

    # The maximum length of the accordion
    return 4 + vertical_count  # 4 for the brackets and colons, plus vertical lines

s = input().strip()
print(max_length_accordion(s))