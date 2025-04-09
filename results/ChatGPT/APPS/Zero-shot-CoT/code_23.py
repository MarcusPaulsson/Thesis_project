def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    str_a = str(a)
    str_b = str(b)
    
    # Generate all unique permutations of a's digits
    perm_set = set(permutations(str_a))
    
    # Filter valid permutations that are less than or equal to b
    valid_numbers = []
    for perm in perm_set:
        perm_number = int(''.join(perm))
        if perm_number <= b and len(str(perm_number)) == len(str_a) and str(perm_number)[0] != '0':
            valid_numbers.append(perm_number)
    
    # Return the maximum valid number found
    return max(valid_numbers)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Calculate and print the result
result = max_permutation_not_exceeding(a, b)
print(result)