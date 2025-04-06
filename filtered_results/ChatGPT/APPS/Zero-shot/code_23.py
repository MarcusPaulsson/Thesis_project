from itertools import permutations

def max_permutation_not_exceeding(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Generate all unique permutations of the digits in a
    perm_set = set(permutations(a_str))
    
    # Filter valid permutations that do not start with '0' and are less than or equal to b
    valid_numbers = []
    for perm in perm_set:
        num_str = ''.join(perm)
        if num_str[0] != '0' and int(num_str) <= b:
            valid_numbers.append(int(num_str))
    
    # Return the maximum of the valid numbers
    return max(valid_numbers)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Get the result and print it
result = max_permutation_not_exceeding(a, b)
print(result)