def construct_binary_string(a, b, x):
    # Start with the base pattern
    if x % 2 == 1:
        # If x is odd, start with '1' if we have more '1's, otherwise start with '0'
        start_with_one = b > a
    else:
        # If x is even, start with '0' if we have more '0's, otherwise start with '1'
        start_with_one = a > b

    result = []
    if start_with_one:
        result.append('1')
        b -= 1
    else:
        result.append('0')
        a -= 1

    # Alternate between 0 and 1 to create the required number of transitions
    for _ in range(x // 2):
        if start_with_one:
            result.append('0')
            a -= 1
            result.append('1')
            b -= 1
        else:
            result.append('1')
            b -= 1
            result.append('0')
            a -= 1

    # Add the remaining characters
    result.append('1' * b)
    result.append('0' * a)

    # Join the list into a string and print
    print(''.join(result))

# Read input
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)