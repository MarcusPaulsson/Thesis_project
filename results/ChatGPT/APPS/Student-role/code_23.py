def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    # Convert a to string and get its digits
    str_a = str(a)
    digits = sorted(str_a, reverse=True)  # Sort digits in descending order

    # Generate all unique permutations of the digits
    unique_permutations = set(permutations(digits))

    # Filter permutations to find the maximum valid number not exceeding b
    max_number = -1
    for perm in unique_permutations:
        num = int(''.join(perm))
        if num <= b and str(num)[0] != '0':  # Check if it does not start with zero
            max_number = max(max_number, num)

    return max_number

# Input
a = int(input().strip())
b = int(input().strip())

# Output
print(max_permutation_not_exceeding(a, b))