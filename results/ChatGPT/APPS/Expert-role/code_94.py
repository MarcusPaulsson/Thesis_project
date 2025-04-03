def construct_binary_string(a, b, x):
    # Start with an empty string
    s = []
    
    # Determine the initial character based on the maximum count
    if a > b:
        current_char = '0'
    else:
        current_char = '1'
    
    # The number of transitions we need to create
    transitions = min(x, a + b - 1)
    
    # Create a sequence that ensures we have the desired number of transitions
    for i in range(transitions + 1):
        s.append(current_char)
        # Toggle between '0' and '1'
        current_char = '1' if current_char == '0' else '0'
    
    # Count how many we've added
    added_zeros = s.count('0')
    added_ones = s.count('1')
    
    # Fill in the remaining zeros or ones
    if current_char == '0':
        remaining = a - added_zeros
        s += ['0'] * remaining
        remaining = b - added_ones
        s += ['1'] * remaining
    else:
        remaining = b - added_ones
        s += ['1'] * remaining
        remaining = a - added_zeros
        s += ['0'] * remaining
    
    # Join the list into a string and print it
    print(''.join(s))

# Read input
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)