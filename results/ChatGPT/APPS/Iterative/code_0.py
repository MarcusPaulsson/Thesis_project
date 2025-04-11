def max_acordion_length(s):
    n = len(s)
    max_length = -1
    left_bracket = -1

    for i in range(n):
        if s[i] == '[':
            left_bracket = i
        elif s[i] == ']' and left_bracket != -1:
            # Count the number of ':' and '|' between the brackets
            colon_count = 0
            pipe_count = 0
            for j in range(left_bracket + 1, i):
                if s[j] == ':':
                    colon_count += 1
                elif s[j] == '|':
                    pipe_count += 1
            if colon_count >= 2:
                # We can form an accordion
                length = 2 + pipe_count + 2  # [ : | : ]
                max_length = max(max_length, length)
            # Reset left_bracket after processing a right bracket
            left_bracket = -1

    return max_length

s = input().strip()
result = max_acordion_length(s)
print(result)