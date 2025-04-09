def construct_binary_string(a, b, x):
    result = []
    
    # Determine the starting character
    if x % 2 == 0:
        start_with_zero = True
    else:
        start_with_zero = False
    
    # Initialize the result based on starting character
    if start_with_zero:
        if a > 0:
            result.append('0')
            a -= 1
        else:
            result.append('1')
            b -= 1
    else:
        if b > 0:
            result.append('1')
            b -= 1
        else:
            result.append('0')
            a -= 1

    # Alternate between 0 and 1 for x transitions
    for _ in range(x):
        if result[-1] == '0' and b > 0:
            result.append('1')
            b -= 1
        elif result[-1] == '1' and a > 0:
            result.append('0')
            a -= 1
            
    # Fill the rest with the last character
    last_char = result[-1]
    while a > 0 or b > 0:
        if last_char == '0' and b > 0:
            result.append('1')
            b -= 1
            last_char = '1'
        elif last_char == '1' and a > 0:
            result.append('0')
            a -= 1
            last_char = '0'

    return ''.join(result)

# Read input values
a, b, x = map(int, input().split())
# Print the result
print(construct_binary_string(a, b, x))