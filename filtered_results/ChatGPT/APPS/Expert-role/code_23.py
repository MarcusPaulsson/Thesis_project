def max_permutation_less_than_b(a, b):
    from itertools import permutations

    # Convert a to string and create a list of its digits
    a_str = str(a)
    b_str = str(b)

    # Generate all unique permutations of the digits of a
    perms = set(permutations(a_str))

    # Filter permutations to find the maximum valid one not exceeding b
    max_valid = -1
    for perm in perms:
        # Join the tuple of characters back into a string
        perm_number = int(''.join(perm))
        # Check if it's valid
        if perm_number <= b and str(perm_number)[0] != '0' and len(str(perm_number)) == len(a_str):
            max_valid = max(max_valid, perm_number)

    return max_valid

# Read input
a = int(input().strip())
b = int(input().strip())

# Get the result and print it
result = max_permutation_less_than_b(a, b)
print(result)