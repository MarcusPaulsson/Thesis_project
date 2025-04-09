def construct_binary_string(a, b, x):
    # Start by determining the base pattern of alternating zeros and ones
    pattern = []
    
    # Determine the starting character based on the greater count
    if a > b:
        start_char = '0'
        switch_char = '1'
    else:
        start_char = '1'
        switch_char = '0'
    
    # Calculate how many switches we need
    switches = min(x, a + b - 1)
    
    # Add the alternating pattern
    for i in range(switches + 1):
        pattern.append(start_char if i % 2 == 0 else switch_char)
    
    # Count the number of zeros and ones used in the alternating pattern
    used_a = pattern.count('0')
    used_b = pattern.count('1')
    
    # Calculate remaining zeros and ones
    remaining_a = a - used_a
    remaining_b = b - used_b
    
    # Fill in the remaining zeros or ones as needed
    if remaining_a > 0:
        pattern.append('0' * remaining_a)
    if remaining_b > 0:
        pattern.append('1' * remaining_b)
    
    # Join the pattern to form the final binary string
    result = ''.join(pattern)
    
    # Print the result
    print(result)

# Read input values
a, b, x = map(int, input().split())

# Construct and print the binary string
construct_binary_string(a, b, x)