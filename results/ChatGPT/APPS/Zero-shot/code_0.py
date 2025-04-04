def max_accordion_length(s):
    first_colon = -1
    last_colon = -1
    opening_bracket = -1
    closing_bracket = -1

    for i in range(len(s)):
        if s[i] == '[' and opening_bracket == -1:
            opening_bracket = i
        elif s[i] == ':' and first_colon == -1:
            first_colon = i
        elif s[i] == ':' and opening_bracket != -1:
            last_colon = i
        elif s[i] == ']' and opening_bracket != -1:
            closing_bracket = i

    if opening_bracket == -1 or first_colon == -1 or last_colon == -1 or closing_bracket == -1:
        return -1

    if first_colon < opening_bracket or last_colon < first_colon or closing_bracket < last_colon:
        return -1

    # Count vertical lines between the first and last colon
    vertical_lines = sum(1 for char in s[first_colon:last_colon] if char == '|')

    # The length of the accordion will be 4 (for the brackets and colons) + vertical lines
    return 4 + vertical_lines

# Read input
s = input().strip()
# Output the result
print(max_accordion_length(s))