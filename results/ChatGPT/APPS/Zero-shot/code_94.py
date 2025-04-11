def construct_binary_string(a, b, x):
    # Start with an empty string
    s = []
    
    # Determine the starting character based on the number of 0s and 1s
    if a > b:
        s.append('0')
        a -= 1
    else:
        s.append('1')
        b -= 1
    
    # We need to create x transitions
    for i in range(x):
        if s[-1] == '0':
            s.append('1')
            b -= 1
        else:
            s.append('0')
            a -= 1
    
    # Now we have used x transitions, we need to fill the rest
    # Fill with the remaining characters
    while a > 0:
        s.append('0')
        a -= 1
    while b > 0:
        s.append('1')
        b -= 1
    
    # Join the list into a string and print it
    print(''.join(s))

# Read input
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)