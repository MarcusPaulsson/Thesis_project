def construct_binary_string(a, b, x):
    # Start with the string made of alternating characters
    result = []
    
    # Determine the initial character based on the counts
    if a > b:
        result.append('0')
        a -= 1
    else:
        result.append('1')
        b -= 1

    # We will create exactly x transitions
    for _ in range(x):
        if result[-1] == '0':
            result.append('1')
            b -= 1
        else:
            result.append('0')
            a -= 1

    # Fill the remaining characters
    if result[-1] == '0':
        result.extend(['0'] * a)
        result.extend(['1'] * b)
    else:
        result.extend(['1'] * b)
        result.extend(['0'] * a)

    return ''.join(result)

# Read input
a, b, x = map(int, input().split())
# Print the output
print(construct_binary_string(a, b, x))