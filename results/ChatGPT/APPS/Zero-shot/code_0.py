def max_length_accordion(s):
    n = len(s)
    left_bracket_index = -1
    right_bracket_index = -1
    
    for i in range(n):
        if s[i] == '[':
            left_bracket_index = i
            break
            
    for i in range(n - 1, -1, -1):
        if s[i] == ']':
            right_bracket_index = i
            break
            
    if left_bracket_index == -1 or right_bracket_index == -1 or left_bracket_index >= right_bracket_index:
        return -1
    
    # Now we need to check for colons and vertical bars between the brackets
    colon_count = 0
    pipe_count = 0
    found_first_colon = False
    
    for i in range(left_bracket_index + 1, right_bracket_index):
        if s[i] == ':':
            if not found_first_colon:
                found_first_colon = True
                colon_count += 1
            else:
                if pipe_count > 0:
                    # We found the second colon after some pipes
                    colon_count += 1
                    break
        elif s[i] == '|':
            if found_first_colon:
                pipe_count += 1
    
    if colon_count < 2:
        return -1
    
    # The length of the accordion is the brackets and the colons plus the pipes
    return 2 + colon_count + pipe_count

# Read input
s = input().strip()
# Calculate and print the result
print(max_length_accordion(s))