from itertools import permutations

def max_permutation_not_exceeding(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Generate all unique permutations of the digits of a
    permuted_numbers = set(int(''.join(p)) for p in permutations(a_str))
    
    # Filter out numbers that are greater than b and have the same length as a
    valid_numbers = [num for num in permuted_numbers if num <= b and len(str(num)) == len(a_str)]
    
    # Return the maximum valid number
    return max(valid_numbers)

# Input
a = int(input().strip())
b = int(input().strip())

# Output
print(max_permutation_not_exceeding(a, b))