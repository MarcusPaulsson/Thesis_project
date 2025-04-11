def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    a_str = str(a)
    b_str = str(b)

    # Generate all unique permutations of the digits of a
    permuted_numbers = sorted(set(int(''.join(p)) for p in permutations(a_str)), reverse=True)

    # Find the maximum permutation that does not exceed b
    for num in permuted_numbers:
        if num <= b and len(str(num)) == len(a_str):
            return num

# Input reading
a = int(input().strip())
b = int(input().strip())

# Output the result
print(max_permutation_not_exceeding(a, b))