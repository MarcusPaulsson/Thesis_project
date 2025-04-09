def max_number_after_replacement(n, a, f):
    # Convert the function f into a mapping from digit to its replacement
    f_map = {str(i + 1): str(f[i]) for i in range(9)}
    
    # Initialize a variable to hold the result
    result = []
    # Flag to indicate whether we are currently replacing digits
    replacing = False
    
    for digit in a:
        if not replacing and f_map[digit] > digit:
            # Start replacing if we find a digit that can be increased
            replacing = True
            result.append(f_map[digit])
        elif replacing:
            if f_map[digit] >= digit:
                # Continue replacing if the replacement is greater than or equal
                result.append(f_map[digit])
            else:
                # Stop replacing if the replacement is less
                result.append(digit)
                replacing = False
        else:
            # If not replacing, just append the original digit
            result.append(digit)
    
    return ''.join(result)

# Read input
n = int(input())
a = input().strip()
f = list(map(int, input().strip().split()))

# Get the result and print it
print(max_number_after_replacement(n, a, f))