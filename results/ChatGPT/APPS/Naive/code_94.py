def construct_binary_string(a, b, x):
    # Initialize the result string
    result = []
    
    # Determine the primary character based on counts
    if a > b:
        primary, secondary = '0', '1'
        primary_count, secondary_count = a, b
    else:
        primary, secondary = '1', '0'
        primary_count, secondary_count = b, a
    
    # Start building the string
    # We need to alternate at least x times
    for i in range(x):
        result.append(primary)
        result.append(secondary)
        primary_count -= 1
        secondary_count -= 1
    
    # At this point, we should have used (x + 1) characters
    # If we have remaining primary characters, append them
    if primary_count > 0:
        result.append(primary * primary_count)
    
    # If we have remaining secondary characters, append them
    if secondary_count > 0:
        result.append(secondary * secondary_count)
    
    # Join the list into a string and print
    print(''.join(result))

# Input reading
a, b, x = map(int, input().split())
construct_binary_string(a, b, x)