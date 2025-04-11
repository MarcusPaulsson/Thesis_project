def max_permutation_not_exceeding(a: int, b: int) -> int:
    from itertools import permutations

    str_a = str(a)
    str_b = str(b)
    
    # Generate all unique permutations of the digits of a
    permuted_numbers = set(int(''.join(p)) for p in permutations(str_a))
    
    # Filter valid numbers that are less than or equal to b and have the same length as a
    valid_numbers = [num for num in permuted_numbers if num <= b and len(str(num)) == len(str_a) and str(num)[0] != '0']
    
    # Return the maximum valid number
    return max(valid_numbers)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Output the result
print(max_permutation_not_exceeding(a, b))