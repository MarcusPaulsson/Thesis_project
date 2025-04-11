def construct_binary_string(a, b, x):
    # Start with an empty list to build the string
    result = []
    
    # Determine the starting character based on the number of zeros and ones
    if a > b:
        result.append('0')
        a -= 1
    else:
        result.append('1')
        b -= 1
    
    # We need to create x transitions
    for _ in range(x):
        if result[-1] == '0':
            result.append('1')
            b -= 1
        else:
            result.append('0')
            a -= 1
    
    # Now we have used x transitions, we need to fill the rest
    while a > 0 or b > 0:
        if result[-1] == '0' and b > 0:
            result.append('1')
            b -= 1
        elif result[-1] == '1' and a > 0:
            result.append('0')
            a -= 1
        elif a > 0:
            result.append('0')
            a -= 1
        elif b > 0:
            result.append('1')
            b -= 1
    
    # Join the list into a string and return
    return ''.join(result)

# Read input
a, b, x = map(int, input().split())
# Construct and print the binary string
print(construct_binary_string(a, b, x))