def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    # Convert a to string to handle its digits
    str_a = str(a)
    str_b = str(b)

    # Generate all unique permutations of the digits in a
    perms = set(permutations(str_a))

    # Filter permutations that do not exceed b and do not start with '0'
    valid_numbers = [
        int(''.join(p)) for p in perms
        if (''.join(p)[0] != '0' and int(''.join(p)) <= b)
    ]

    # Return the maximum valid number
    return max(valid_numbers)

# Read input
a = int(input().strip())
b = int(input().strip())

# Get the result
result = max_permutation_not_exceeding(a, b)

# Print the result
print(result)