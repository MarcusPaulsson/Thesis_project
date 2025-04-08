def construct_binary_string(a, b, x):
    # Initialize the binary string as a list of characters
    result = []
    
    # Determine the starting character based on the majority
    current_char = '0' if a >= b else '1'
    
    # Create the alternating pattern required to satisfy the x transitions
    for _ in range(x + 1):
        result.append(current_char)
        current_char = '1' if current_char == '0' else '0'
    
    # Count how many zeros and ones we have used
    zeros_used = result.count('0')
    ones_used = result.count('1')
    
    # Populate the remaining characters
    while zeros_used < a or ones_used < b:
        if zeros_used < a:
            result.append('0')
            zeros_used += 1
        if ones_used < b:
            result.append('1')
            ones_used += 1
            
    return ''.join(result)

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))