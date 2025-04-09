def maxAccordionLength(s: str) -> int:
    n = len(s)
    
    # Find the last occurrence of the opening bracket '['
    left_bracket_index = s.rfind('[')
    # Find the first occurrence of the closing bracket ']'
    right_bracket_index = s.find(']', left_bracket_index)
    
    # If there's no valid brackets or they are in the wrong order, return -1
    if left_bracket_index == -1 or right_bracket_index == -1 or left_bracket_index >= right_bracket_index:
        return -1

    # Count the number of ':' and '|' between the brackets
    colon_count = s[left_bracket_index + 1:right_bracket_index].count(':')
    pipe_count = s[left_bracket_index + 1:right_bracket_index].count('|')

    # There must be at least 2 colons and at least 0 pipes
    if colon_count < 2:
        return -1

    # The maximum length is the length of the brackets plus the pipes and colons
    max_length = (right_bracket_index - left_bracket_index + 1)  # Length of '[::]'
    return max_length

# Read input and output the result
s = input().strip()
print(maxAccordionLength(s))