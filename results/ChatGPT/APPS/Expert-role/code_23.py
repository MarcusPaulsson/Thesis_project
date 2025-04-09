def max_permutation_not_exceeding(a, b):
    from itertools import permutations
    
    # Convert numbers to string to work with digits
    str_a = str(a)
    str_b = str(b)
    
    # Get all unique permutations of the digits of a
    unique_permutations = sorted(set(permutations(str_a)), reverse=True)
    
    # Find the largest permutation that does not exceed b
    for perm in unique_permutations:
        candidate = int(''.join(perm))
        if candidate <= b:
            return candidate
    
    return None  # This should not happen as per the problem statement

# Input reading
a = int(input().strip())
b = int(input().strip())

# Get the result and print it
result = max_permutation_not_exceeding(a, b)
print(result)