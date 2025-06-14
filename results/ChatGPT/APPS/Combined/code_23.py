def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    a_str = str(a)
    b_str = str(b)

    # Generate all unique permutations of the digits of a
    permuted_numbers = set(int(''.join(p)) for p in permutations(a_str))

    # Filter permutations to find the maximum that does not exceed b
    valid_numbers = [num for num in permuted_numbers if num <= b and len(str(num)) == len(a_str)]

    return max(valid_numbers)

# Input reading
a = int(input().strip())
b = int(input().strip())

# Get the result and print it
result = max_permutation_not_exceeding(a, b)
print(result)