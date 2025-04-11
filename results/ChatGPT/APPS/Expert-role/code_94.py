def construct_binary_string(a, b, x):
    # Start with the base pattern
    if x % 2 == 0:
        pattern = '01' * (x // 2)
    else:
        pattern = '01' * (x // 2) + '0'
    
    # Count how many zeros and ones are used
    used_zeros = pattern.count('0')
    used_ones = pattern.count('1')
    
    # Remaining zeros and ones
    remaining_zeros = a - used_zeros
    remaining_ones = b - used_ones
    
    # Add remaining zeros and ones to the end of the pattern
    if remaining_zeros > 0:
        pattern += '0' * remaining_zeros
    if remaining_ones > 0:
        pattern += '1' * remaining_ones
    
    # If we have more than one segment, we need to ensure we don't exceed x transitions
    if x < a + b - 1:
        # We need to adjust the pattern to ensure exactly x transitions
        if remaining_zeros > 0 and remaining_ones > 0:
            # We can add a block of zeros or ones to reduce transitions
            if pattern[-1] == '0':
                pattern += '0' * (remaining_zeros - 1)
            else:
                pattern += '1' * (remaining_ones - 1)
    
    return pattern

# Read input
a, b, x = map(int, input().split())
# Construct and print the binary string
print(construct_binary_string(a, b, x))