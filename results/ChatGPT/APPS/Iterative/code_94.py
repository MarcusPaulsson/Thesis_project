def construct_binary_string(a, b, x):
    # Determine the starting character based on the parity of x
    start_with_one = (x % 2 == 1 and b > 0) or (x % 2 == 0 and a == 0)

    # Initialize the result list
    result = []
    
    # Determine the initial character
    current_char = '1' if start_with_one else '0'
    
    # Alternate characters for x transitions
    for i in range(x):
        result.append(current_char)
        current_char = '0' if current_char == '1' else '1'
    
    # Count how many 0s and 1s we have used
    used_zeros = result.count('0')
    used_ones = result.count('1')
    
    # Calculate remaining 0s and 1s
    remaining_zeros = a - used_zeros
    remaining_ones = b - used_ones
    
    # Add remaining characters to the end of the result
    if current_char == '0':
        result.append('0' * remaining_zeros)
        result.append('1' * remaining_ones)
    else:
        result.append('1' * remaining_ones)
        result.append('0' * remaining_zeros)
    
    # Join the result list into a string
    return ''.join(result)

# Read input
a, b, x = map(int, input().split())

# Construct and print the binary string
print(construct_binary_string(a, b, x))