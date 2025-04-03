def construct_binary_string(a, b, x):
    # Start with the maximum alternation
    s = []
    
    # Calculate the number of segments
    num_segments = x + 1
    
    # Determine how many 0s and 1s to distribute in segments
    zero_segments = min(num_segments, a + 1)
    one_segments = min(num_segments, b + 1)
    
    # Calculate the number of 0s and 1s per segment
    zeros_per_segment = a // zero_segments
    ones_per_segment = b // one_segments
    
    # Calculate the remaining 0s and 1s after even distribution
    remaining_zeros = a % zero_segments
    remaining_ones = b % one_segments
    
    # Build the segments
    for i in range(num_segments):
        if i % 2 == 0:  # Even index - place 0s
            count = zeros_per_segment + (1 if i < remaining_zeros else 0)
            s.append('0' * count)
        else:  # Odd index - place 1s
            count = ones_per_segment + (1 if i < remaining_ones else 0)
            s.append('1' * count)
    
    # Join the segments into a single string
    result = ''.join(s)
    
    # If the length of the result is not exactly a + b, adjust by trimming
    if len(result) > a + b:
        result = result[:a + b]
    
    return result

# Read input
a, b, x = map(int, input().split())

# Generate and print the binary string
print(construct_binary_string(a, b, x))