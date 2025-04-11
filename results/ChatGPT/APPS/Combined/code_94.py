def construct_binary_string(a, b, x):
    # Initialize the result list
    result = []
    
    # Determine the starting character based on the counts of a and b
    if a > b:
        current_char = '0'
        a -= 1
    else:
        current_char = '1'
        b -= 1
    
    # Create the alternating pattern based on x transitions
    for _ in range(x):
        result.append(current_char)
        if current_char == '0':
            current_char = '1'
            b -= 1
        else:
            current_char = '0'
            a -= 1
    
    # Append remaining characters
    result.extend(['0'] * a)
    result.extend(['1'] * b)
    
    # Join the list into a string and return
    return ''.join(result)

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))