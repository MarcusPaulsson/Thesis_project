def construct_binary_string(a, b, x):
    # Start with an empty list to build the string
    s = []
    
    # Determine the starting character based on the counts of 0s and 1s
    if a + b < x + 1 or (x % 2 == 1 and (a == 0 or b == 0)):
        print("Impossible to construct the string with the given parameters.")
        return
    
    is_zero_turn = a >= b  # Start with '0' if more or equal zeros than ones
    for i in range(x + 1):
        if is_zero_turn:
            if a > 0:
                s.append('0')
                a -= 1
            is_zero_turn = False
        else:
            if b > 0:
                s.append('1')
                b -= 1
            is_zero_turn = True
            
    # Fill the rest with the remaining characters
    s.extend(['0'] * a)
    s.extend(['1'] * b)
    
    # Join the list into a string and print it
    print(''.join(s))

# Input reading
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)