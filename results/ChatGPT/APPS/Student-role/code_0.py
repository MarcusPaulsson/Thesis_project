def max_acc_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    colon_count = 0
    pipe_count = 0

    for i in range(n):
        if s[i] == '[' and left_bracket == -1:
            left_bracket = i
        elif s[i] == ':' and left_bracket != -1:
            colon_count += 1
        elif s[i] == ']' and left_bracket != -1:
            right_bracket = i
            break

    if left_bracket == -1 or right_bracket == -1 or right_bracket < left_bracket:
        return -1

    # Count pipes between the first colon after the left bracket and the second colon before the right bracket
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == '|':
            pipe_count += 1
        elif s[i] == ':':
            # We should only count pipes between the two colons
            colon_count -= 1

    if colon_count < 2:
        return -1

    # The maximum length of the accordion
    return 4 + pipe_count

# Example usage:
s = input().strip()
print(max_acc_length(s))