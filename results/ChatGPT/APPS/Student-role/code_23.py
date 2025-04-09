from itertools import permutations

def max_permutation_not_exceeding(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Generate all unique permutations of the digits of a
    perm_set = set(permutations(a_str))
    
    # Filter permutations that are valid (do not have leading zero)
    valid_numbers = []
    for perm in perm_set:
        num_str = ''.join(perm)
        if num_str[0] != '0' and len(num_str) == len(a_str):
            valid_numbers.append(int(num_str))
    
    # Find the maximum permutation that does not exceed b
    max_valid = -1
    for num in valid_numbers:
        if num <= b:
            max_valid = max(max_valid, num)
    
    return max_valid

# Input reading
a = int(input().strip())
b = int(input().strip())

# Get the result
result = max_permutation_not_exceeding(a, b)

# Output the result
print(result)