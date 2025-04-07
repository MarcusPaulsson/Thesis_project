def construct_binary_string(a, b, x):
    # Initialize the string
    s = []
    
    # Determine the starting character
    if a > b:
        s.append('0')
        a -= 1
    else:
        s.append('1')
        b -= 1

    # Current segments of different characters
    current_segments = 1

    # Add alternating characters until we reach x
    while current_segments < x and (a > 0 or b > 0):
        if s[-1] == '0' and b > 0:
            s.append('1')
            b -= 1
        elif s[-1] == '1' and a > 0:
            s.append('0')
            a -= 1
        current_segments += 1

    # Fill the remaining with the last character
    last_char = s[-1]
    remaining_count = a if last_char == '0' else b
    s.extend([last_char] * remaining_count)
    s.extend(['1' if last_char == '0' else '0'] * (b if last_char == '0' else a))

    return ''.join(s)

# Read input values
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))