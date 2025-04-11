def construct_binary_string(a, b, x):
    # Initialize the binary string
    s = []
    
    # Determine the starting character based on the larger count
    current_char = '0' if a >= b else '1'
    s.append(current_char)
    
    # Adjust counts
    if current_char == '0':
        a -= 1
    else:
        b -= 1

    # Fill the string with alternating characters until we reach x transitions
    for _ in range(x):
        next_char = '1' if current_char == '0' else '0'
        s.append(next_char)
        
        if next_char == '0':
            a -= 1
        else:
            b -= 1
        
        current_char = next_char

    # Fill the remaining characters with the last used character
    while a > 0 or b > 0:
        if current_char == '0' and a > 0:
            s.append('0')
            a -= 1
        elif current_char == '1' and b > 0:
            s.append('1')
            b -= 1
        
        # Switch current_char if we can add the other character
        if current_char == '0' and b > 0:
            current_char = '1'
        elif current_char == '1' and a > 0:
            current_char = '0'

    return ''.join(s)

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))