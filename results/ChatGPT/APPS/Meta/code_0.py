def max_acc_length(s):
    n = len(s)
    left_bracket = -1
    first_colon = -1
    second_colon = -1
    right_bracket = -1

    # Find the positions of the brackets and colons
    for i in range(n):
        if s[i] == '[' and left_bracket == -1:
            left_bracket = i
        elif s[i] == ':' and left_bracket != -1 and first_colon == -1:
            first_colon = i
        elif s[i] == ':' and first_colon != -1 and second_colon == -1:
            second_colon = i
        elif s[i] == ']' and second_colon != -1 and right_bracket == -1:
            right_bracket = i
            break

    # Check if we found a valid accordion structure
    if left_bracket != -1 and first_colon != -1 and second_colon != -1 and right_bracket != -1:
        # Count the number of '|' characters between the first and second colon
        num_pipes = s[first_colon + 1:second_colon].count('|')
        # Calculate the length of the accordion
        accordion_length = 4 + num_pipes
        return accordion_length
    else:
        return -1

# Example usage
s = input().strip()
print(max_acc_length(s))