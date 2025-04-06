def max_permutation_not_exceeding(a, b):
    from itertools import permutations
    
    a_str = str(a)
    permuted_numbers = {int(''.join(p)) for p in permutations(a_str)}  # Use set comprehension for uniqueness
    
    # Use a generator to find valid numbers without creating a complete list
    valid_numbers = (num for num in permuted_numbers if num <= b and len(str(num)) == len(a_str))
    
    # Return the maximum of the valid numbers, or None if no valid numbers exist
    return max(valid_numbers, default=None)

# Read input
a = int(input().strip())
b = int(input().strip())

# Get the result
result = max_permutation_not_exceeding(a, b)

# Print the result or a message if no valid permutation exists
print(result if result is not None else "No valid permutation found")