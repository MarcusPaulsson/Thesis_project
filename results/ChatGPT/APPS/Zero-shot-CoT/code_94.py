def construct_binary_string(a, b, x):
    # Start with the maximum number of transitions
    transitions = min(x, a + b - 1)
    
    # Determine the base pattern
    pattern = []
    if transitions % 2 == 0:
        # Start with 0 if we have an even number of transitions
        start_with_zero = True
    else:
        # Start with 1 if we have an odd number of transitions
        start_with_zero = False
    
    # Create the alternating pattern
    for i in range(transitions + 1):
        if (i % 2 == 0) == start_with_zero:
            pattern.append('0')
        else:
            pattern.append('1')
    
    # Count how many 0s and 1s we have used
    used_zeros = pattern.count('0')
    used_ones = pattern.count('1')
    
    # Calculate remaining 0s and 1s
    remaining_zeros = a - used_zeros
    remaining_ones = b - used_ones
    
    # Fill the remaining 0s and 1s
    if remaining_zeros > 0:
        if pattern[0] == '0':
            pattern = ['0'] * remaining_zeros + pattern
        else:
            pattern = ['0'] * remaining_zeros + pattern + ['0'] * remaining_zeros
    
    if remaining_ones > 0:
        if pattern[0] == '1':
            pattern = ['1'] * remaining_ones + pattern
        else:
            pattern = ['1'] * remaining_ones + pattern + ['1'] * remaining_ones
    
    # Join the pattern into a string
    result = ''.join(pattern)
    
    # Ensure the string has exactly a zeros and b ones
    result = result[:a + b]
    
    return result

# Input reading
a, b, x = map(int, input().split())
# Output the result
print(construct_binary_string(a, b, x))