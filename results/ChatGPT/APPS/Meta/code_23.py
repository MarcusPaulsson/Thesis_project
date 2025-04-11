def max_permutation_not_exceeding(a, b):
    from itertools import permutations
    
    # Convert a to string to work with its digits
    str_a = str(a)
    str_b = str(b)
    
    # Generate all unique permutations of the digits of a
    permuted_numbers = set(int(''.join(p)) for p in permutations(str_a))
    
    # Filter out numbers that are greater than b and have the same length as a
    valid_numbers = [num for num in permuted_numbers if num <= b and len(str(num)) == len(str_a)]
    
    # Return the maximum of the valid numbers
    return max(valid_numbers)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Output the result
print(max_permutation_not_exceeding(a, b))