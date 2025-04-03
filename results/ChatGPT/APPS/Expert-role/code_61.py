def max_transformed_number(n, a, f):
    # Convert the function into a mapping from digit to its transformed value
    f_map = {str(i + 1): str(f[i]) for i in range(9)}
    
    # Create a list to store the transformed number
    transformed = []
    transformation_started = False
    
    for digit in a:
        if not transformation_started and f_map[digit] > digit:
            # Start transforming if the current digit can be improved
            transformation_started = True
        if transformation_started:
            # Replace the digit with its transformed value
            transformed.append(f_map[digit])
        else:
            transformed.append(digit)
    
    # If we finished transforming and the transformation was started
    # We should ensure we keep transforming till the end if it's beneficial
    if transformation_started:
        for i in range(len(transformed)):
            if transformed[i] < a[i]:
                break
            transformed[i] = f_map[a[i]]
    
    result = ''.join(transformed)
    return result

# Input reading
n = int(input().strip())
a = input().strip()
f = list(map(int, input().strip().split()))

# Getting the result
result = max_transformed_number(n, a, f)

# Printing the result
print(result)