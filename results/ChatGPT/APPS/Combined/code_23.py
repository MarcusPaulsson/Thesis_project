def max_permutation_not_exceeding(a: int, b: int) -> int:
    from itertools import permutations

    str_a = str(a)
    str_b = str(b)

    # Generate all unique permutations of the digits of a
    unique_permutations = sorted(set(permutations(str_a)), reverse=True)

    for p in unique_permutations:
        candidate = int(''.join(p))
        # Check if the candidate is less than or equal to b and has the same length as a
        if candidate <= b and len(str(candidate)) == len(str_a):
            return candidate

# Input reading
a = int(input().strip())
b = int(input().strip())

# Function call and output
print(max_permutation_not_exceeding(a, b))