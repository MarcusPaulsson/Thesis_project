def construct_binary_string(a, b, x):
    # Start with an empty list to build the binary string
    s = []
    
    # Determine the initial character based on the counts of a and b
    if a > b:
        s.append('0')
        a -= 1
    else:
        s.append('1')
        b -= 1
    
    # Add alternating characters to reach the required `x`
    for _ in range(x):
        if s[-1] == '0':
            s.append('1')
            b -= 1
        else:
            s.append('0')
            a -= 1
            
    # Now fill the remaining characters
    # If the last character is '0', we need to fill with '0's
    if s[-1] == '0':
        s.extend(['0'] * a)
        s.extend(['1'] * b)
    else:
        s.extend(['1'] * b)
        s.extend(['0'] * a)
    
    return ''.join(s)

# Read input
a, b, x = map(int, input().split())

# Generate and print the binary string
result = construct_binary_string(a, b, x)
print(result)