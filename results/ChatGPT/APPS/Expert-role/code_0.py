def max_acordion_length(s):
    n = len(s)
    left_bracket_index = -1
    right_bracket_index = -1
    max_length = -1

    for i in range(n):
        if s[i] == '[':
            left_bracket_index = i
        elif s[i] == ']':
            right_bracket_index = i
            if left_bracket_index != -1 and right_bracket_index > left_bracket_index:
                # Count the number of ':' and '|' between the brackets
                colon_count = 0
                pipe_count = 0
                for j in range(left_bracket_index + 1, right_bracket_index):
                    if s[j] == ':':
                        colon_count += 1
                    elif s[j] == '|':
                        pipe_count += 1
                if colon_count >= 2:
                    # Valid accordion found
                    length = 2 + pipe_count  # 2 for the colons and brackets
                    max_length = max(max_length, length)

    return max_length

s = input().strip()
print(max_acordion_length(s))