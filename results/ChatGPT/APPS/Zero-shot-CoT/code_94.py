def construct_binary_string(a, b, x):
    # Start with the base pattern
    if x % 2 == 1:
        # If x is odd, start with '1' if we have more '1's, else start with '0'
        start_with_one = b > a
    else:
        # If x is even, start with '0' if we have more '0's, else start with '1'
        start_with_one = a > b

    # Initialize the string
    s = []
    
    # Fill the string based on the starting character
    if start_with_one:
        s.append('1')
        b -= 1
    else:
        s.append('0')
        a -= 1

    # Alternate between '0' and '1' until we reach x transitions
    for i in range(x):
        if s[-1] == '0':
            s.append('1')
            b -= 1
        else:
            s.append('0')
            a -= 1

    # Now fill the rest with the remaining characters
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