def max_length_accordion(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    colon_count = 0
    vertical_count = 0
    
    for i in range(n):
        if s[i] == '[':
            left_bracket = i
            break
            
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket = i
            break
            
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1
    
    for i in range(left_bracket, right_bracket + 1):
        if s[i] == ':':
            colon_count += 1
        elif s[i] == '|':
            vertical_count += 1
            
    if colon_count < 2:
        return -1
    
    # The maximum length of the accordion is 2 colons + vertical lines
    return 2 + vertical_count

s = input().strip()
print(max_length_accordion(s))