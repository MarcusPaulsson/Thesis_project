def construct_binary_string(a, b, x):
    # Start with an empty list for the result
    result = []
    
    # Determine the starting character based on x
    if x % 2 == 1:
        # Start with '1' if x is odd, else start with '0'
        start_with_one = True
    else:
        start_with_one = False
    
    # Fill the string with alternating characters
    while a > 0 or b > 0:
        if (start_with_one and b > 0) or (not start_with_one and a == 0):
            result.append('1')
            b -= 1
        elif (not start_with_one and a > 0) or (start_with_one and b == 0):
            result.append('0')
            a -= 1
        start_with_one = not start_with_one  # Toggle the starting character
    
    # After placing the alternating characters, we may still have some 0s or 1s left
    # Repeat the last added character if there are remaining characters
    if a > 0:
        result.extend('0' * a)
    if b > 0:
        result.extend('1' * b)
    
    return ''.join(result)

# Input reading
a, b, x = map(int, input().split())
# Construct and print the binary string
print(construct_binary_string(a, b, x))