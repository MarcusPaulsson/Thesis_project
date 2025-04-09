def construct_binary_string(a, b, x):
    # Initialize the result list
    result = []
    
    # Determine the starting character based on the counts of a and b
    if a > b:
        current_char = '0'
    else:
        current_char = '1'
    
    # Create the alternating pattern
    for _ in range(x // 2):
        result.append(current_char)
        if current_char == '0':
            current_char = '1'
        else:
            current_char = '0'
    
    # Add the remaining characters of the same type
    if current_char == '0':
        result.append('0' * (a - (x + 1) // 2))
        result.append('1' * (b - x // 2))
    else:
        result.append('1' * (b - (x + 1) // 2))
        result.append('0' * (a - x // 2))
    
    # Join the result and print it
    print(''.join(result))

# Read input values
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)