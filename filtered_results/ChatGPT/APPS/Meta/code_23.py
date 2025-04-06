def max_permuted_not_exceeding(a, b):
    from itertools import permutations

    # Convert numbers to strings to work with digits
    str_a = str(a)
    str_b = str(b)
    
    # Generate all unique permutations of the digits of a
    permuted_numbers = sorted(set(int(''.join(p)) for p in permutations(str_a)), reverse=True)
    
    # Find the maximum number that does not exceed b
    for num in permuted_numbers:
        if num <= b:
            return num

# Read input
a = int(input().strip())
b = int(input().strip())

# Get the result and print it
result = max_permuted_not_exceeding(a, b)
print(result)