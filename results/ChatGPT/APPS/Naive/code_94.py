def construct_binary_string(a, b, x):
    # Initialize the string
    result = []
    
    # Determine the starting character based on the counts of a and b
    if a > b:
        result.append('0')
        a -= 1
    else:
        result.append('1')
        b -= 1
    
    # We need to create x transitions
    for _ in range(x):
        # Alternate between 0 and 1
        if result[-1] == '0':
            result.append('1')
            b -= 1
        else:
            result.append('0')
            a -= 1
    
    # Fill the remaining characters with the last character used
    last_char = result[-1]
    while a > 0 or b > 0:
        if last_char == '0' and a > 0:
            result.append('0')
            a -= 1
        elif last_char == '1' and b > 0:
            result.append('1')
            b -= 1
        # Switch last_char if we just added one
        last_char = result[-1]
    
    return ''.join(result)

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))