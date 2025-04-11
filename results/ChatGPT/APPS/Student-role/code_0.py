def max_acordion_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    colon_count = 0
    pipe_count = 0

    for i in range(n):
        if s[i] == '[':
            left_bracket = i
        elif s[i] == ']':
            right_bracket = i
            if left_bracket != -1 and right_bracket > left_bracket:
                # Count colons and pipes between the brackets
                for j in range(left_bracket + 1, right_bracket):
                    if s[j] == ':':
                        colon_count += 1
                    elif s[j] == '|':
                        pipe_count += 1

    if left_bracket == -1 or right_bracket == -1 or colon_count < 2:
        return -1

    # Maximum length of accordion
    return 4 + pipe_count

s = input().strip()
print(max_acordion_length(s))