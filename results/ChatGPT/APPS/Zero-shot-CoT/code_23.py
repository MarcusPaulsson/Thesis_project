def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    # Convert to string for easier manipulation
    str_a = str(a)
    str_b = str(b)

    # Generate all unique permutations of the digits of a
    permuted_numbers = set(int(''.join(p)) for p in permutations(str_a))
    
    # Filter out numbers that start with 0 and are greater than b
    valid_numbers = [num for num in permuted_numbers if num <= b and str(num)[0] != '0']
    
    # Return the maximum valid number
    return max(valid_numbers)

# Read input
a = int(input().strip())
b = int(input().strip())

# Get the result and print it
result = max_permutation_not_exceeding(a, b)
print(result)