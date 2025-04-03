def max_accordion_length(s):
    n = len(s)
    left_bracket = -1
    right_bracket = -1
    max_length = -1

    # Find the last occurrence of '['
    for i in range(n):
        if s[i] == '[':
            left_bracket = i

    # Find the first occurrence of ']'
    for i in range(n-1, -1, -1):
        if s[i] == ']':
            right_bracket = i

    # If no valid brackets found
    if left_bracket == -1 or right_bracket == -1 or left_bracket >= right_bracket:
        return -1

    # Now we look for the colons and vertical bars
    first_colon = -1
    last_colon = -1
    
    for i in range(left_bracket + 1, right_bracket):
        if s[i] == ':':
            if first_colon == -1:
                first_colon = i
            last_colon = i

    # If we find at least one colon
    if first_colon != -1 and last_colon != -1 and first_colon < last_colon:
        count_bars = s[first_colon + 1:last_colon].count('|')
        max_length = 2 + (last_colon - first_colon - 1) + 2  # [ + : + bars + : + ]
        return max_length

    return -1

# Input
s = input().strip()
# Output
print(max_accordion_length(s))