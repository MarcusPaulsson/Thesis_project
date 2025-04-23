def construct_binary_string(a, b, x):
    # Determine the base pattern based on the number of transitions needed
    pattern = []
    
    # Calculate the number of transitions we can create
    transitions = min(x, a + b - 1)
    
    # Create the alternating pattern
    for i in range(transitions + 1):
        if i % 2 == 0 and a > 0:
            pattern.append('0')
            a -= 1
        elif i % 2 == 1 and b > 0:
            pattern.append('1')
            b -= 1
    
    # Fill the remaining characters
    pattern.append('0' * a)
    pattern.append('1' * b)
    
    # Join the list into a string
    result = ''.join(pattern)
    
    # Return the constructed binary string
    return result

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))