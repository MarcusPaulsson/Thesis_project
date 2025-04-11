def max_permutation_not_exceeding(a, b):
    from itertools import permutations
    
    # Convert a to string to work with its digits
    str_a = str(a)
    str_b = str(b)
    
    # Generate all unique permutations of the digits of a
    perms = set(permutations(str_a))
    
    # Filter out permutations that are valid (not starting with '0' and not exceeding b)
    valid_perms = []
    for perm in perms:
        num = int(''.join(perm))
        if num <= b and str(num) == str_a:  # Check if it has the same length as a
            valid_perms.append(num)
    
    # Return the maximum valid permutation
    return max(valid_perms)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Get the result
result = max_permutation_not_exceeding(a, b)

# Print the result
print(result)