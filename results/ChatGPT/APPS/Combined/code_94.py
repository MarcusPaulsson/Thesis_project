def construct_binary_string(a, b, x):
    # Initialize variables for the result and remaining counts
    result = []
    first_char, second_char = ('0', '1') if a > b else ('1', '0')
    first_count, second_count = (a, b) if a > b else (b, a)

    # Create the alternating pattern
    for _ in range(x):
        if first_count > 0:
            result.append(first_char)
            first_count -= 1
        if second_count > 0:
            result.append(second_char)
            second_count -= 1

    # Add the remaining characters of the majority type
    result.append(first_char * first_count)
    result.append(second_char * second_count)

    # Join the list into a string and return
    return ''.join(result)

# Read input
a, b, x = map(int, input().split())
# Generate and print the binary string
print(construct_binary_string(a, b, x))