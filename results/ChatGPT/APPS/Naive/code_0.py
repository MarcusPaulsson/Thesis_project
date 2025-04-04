def max_length_acordion(s: str) -> int:
    n = len(s)
    
    # Initialize indices for the first opening bracket and the last closing bracket
    first_open = -1
    last_close = -1
    
    # Find the first '[' and the last ']'
    for i in range(n):
        if s[i] == '[' and first_open == -1:
            first_open = i
        if s[i] == ']' and first_open != -1:
            last_close = i
    
    # If we haven't found both brackets, return -1
    if first_open == -1 or last_close == -1 or last_close <= first_open:
        return -1
    
    # Now we need to find the colons and vertical lines
    first_colon = -1
    second_colon = -1
    vertical_count = 0
    
    # Iterate between the first '[' and last ']' to find colons and vertical lines
    for i in range(first_open + 1, last_close):
        if s[i] == ':':
            if first_colon == -1:
                first_colon = i
            elif second_colon == -1:
                second_colon = i
                break  # We found both colons, no need to continue
    
        if s[i] == '|':
            vertical_count += 1
    
    # If we found at least one colon and both colons are in the right order
    if first_colon != -1 and (second_colon == -1 or second_colon > first_colon):
        # Calculate the length of the accordion
        accordion_length = (last_close - first_open + 1) + vertical_count
        return accordion_length
    else:
        return -1

# Read input
s = input().strip()
# Output the result
print(max_length_acordion(s))