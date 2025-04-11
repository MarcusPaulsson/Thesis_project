def construct_binary_string(a, b, x):
    # Start with the base pattern
    pattern = []
    
    # Determine the starting character based on the larger count
    if a > b:
        pattern.append('0')
        a -= 1
    else:
        pattern.append('1')
        b -= 1
    
    # Alternate between 0s and 1s to create the required transitions
    for _ in range(x):
        if pattern[-1] == '0':
            pattern.append('1')
            b -= 1
        else:
            pattern.append('0')
            a -= 1
    
    # Fill the remaining characters with the last used character
    last_char = pattern[-1]
    remaining = a if last_char == '0' else b
    
    pattern.extend([last_char] * remaining)
    
    # Join the list into a string and return
    return ''.join(pattern)

# Input reading
a, b, x = map(int, input().split())
# Output the result
print(construct_binary_string(a, b, x))