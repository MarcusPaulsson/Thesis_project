def construct_binary_string(a, b, x):
    # Start with the first character based on the larger count
    if a > b:
        s = '0'
        a -= 1
    else:
        s = '1'
        b -= 1

    # Alternate between 0s and 1s to create the required number of transitions
    transitions = 0
    while transitions < x:
        if s[-1] == '0' and b > 0:
            s += '1'
            b -= 1
        elif s[-1] == '1' and a > 0:
            s += '0'
            a -= 1
        transitions += 1

    # Fill the rest of the string with the remaining characters
    s += '0' * a + '1' * b
    return s

# Read input
a, b, x = map(int, input().split())
# Construct and print the binary string
print(construct_binary_string(a, b, x))