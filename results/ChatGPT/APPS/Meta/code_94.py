def construct_binary_string(a, b, x):
    # Initialize the binary string
    s = []
    
    # Determine the starting character based on the counts of a and b
    if a > b:
        s.append('0')
        a -= 1
    else:
        s.append('1')
        b -= 1
    
    # We need to create x transitions
    transitions = x
    
    # Create the alternating pattern
    while transitions > 0:
        if s[-1] == '0':
            s.append('1')
            b -= 1
        else:
            s.append('0')
            a -= 1
        transitions -= 1
    
    # Fill the remaining characters
    while a > 0:
        s.append('0')
        a -= 1
    while b > 0:
        s.append('1')
        b -= 1
    
    # Join the list into a string and return
    return ''.join(s)

# Read input
a, b, x = map(int, input().split())
# Print the result
print(construct_binary_string(a, b, x))