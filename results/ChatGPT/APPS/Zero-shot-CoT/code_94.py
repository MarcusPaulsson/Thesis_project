def construct_binary_string(a, b, x):
    # Start with an empty string
    s = []
    
    # Determine the starting character based on the parity of x
    if x % 2 == 1:
        # Start with '1' if x is odd
        current_char = '1'
        b -= 1
    else:
        # Start with '0' if x is even
        current_char = '0'
        a -= 1

    # We need to create x transitions
    for i in range(x):
        s.append(current_char)
        # Alternate between '0' and '1'
        current_char = '0' if current_char == '1' else '1'
    
    # After x transitions, we need to fill the rest of the string
    if current_char == '0':
        # Fill with remaining zeros
        s.append('0' * a)
        s.append('1' * b)
    else:
        # Fill with remaining ones
        s.append('1' * b)
        s.append('0' * a)

    # Join the list to form the final string
    return ''.join(s)

# Input
a, b, x = map(int, input().split())
# Output the constructed string
print(construct_binary_string(a, b, x))