def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    # Convert a to a string to work with its digits
    a_str = str(a)
    
    # Generate all unique permutations of the digits of a
    perm_set = set(permutations(a_str))
    
    # Filter permutations to find valid candidates not exceeding b
    valid_candidates = []
    for perm in perm_set:
        # Join the tuple of characters back into a string and convert to int
        num = int(''.join(perm))
        if num <= b and str(num)[0] != '0' and len(str(num)) == len(a_str):
            valid_candidates.append(num)
    
    # Return the maximum value found
    return max(valid_candidates)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Output the result
print(max_permutation_not_exceeding(a, b))