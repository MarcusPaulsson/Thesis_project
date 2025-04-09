def maximum_number_after_operation(n, a, f):
    # Convert f to a list of integers for easier indexing
    f = [0] + f  # f[0] is not used, f[1] corresponds to index 1
    
    # Create a list to hold the result
    result = list(a)
    
    # Flag to check if we've started replacing
    replacing = False
    
    for i in range(n):
        original_digit = int(a[i])
        new_digit = f[original_digit]
        
        # Start replacing when we find a digit that can be replaced
        if new_digit > original_digit:
            replacing = True
            result[i] = str(new_digit)
        elif new_digit < original_digit and replacing:
            # If we are replacing and found a digit where replacement doesn't enhance, stop
            break
        elif replacing:
            # Continue replacing if we are already in a replacement phase
            result[i] = str(new_digit)
    
    # Join the result and return the maximum number as a string
    return ''.join(result)

# Read input
n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the maximum number possible after the operation
max_number = maximum_number_after_operation(n, a, f)

# Print the result
print(max_number)