def construct_binary_string(a, b, x):
    # Determine the base pattern based on x
    if x % 2 == 0:
        pattern = '01' * (x // 2)
    else:
        pattern = '01' * (x // 2) + '0'
    
    # Count how many 0s and 1s are used in the pattern
    used_0s = pattern.count('0')
    used_1s = pattern.count('1')
    
    # Calculate remaining 0s and 1s
    remaining_0s = a - used_0s
    remaining_1s = b - used_1s
    
    # Add remaining 0s or 1s to the end of the pattern
    if remaining_0s > 0:
        pattern += '0' * remaining_0s
    if remaining_1s > 0:
        pattern += '1' * remaining_1s
    
    # If we have more 1s than 0s, we need to ensure we start with 1
    if b > a:
        pattern = pattern.replace('0', 'x').replace('1', '0').replace('x', '1')
    
    return pattern

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))