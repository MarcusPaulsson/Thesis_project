def max_permutation_not_exceeding(a, b):
    from itertools import permutations

    str_a = str(a)
    str_b = str(b)
    
    # Generate all unique permutations of digits in a
    perm = sorted(set(permutations(str_a)), reverse=True)
    
    for p in perm:
        num = int(''.join(p))
        # Check if the permutation is less than or equal to b and has the same length as a
        if num <= b and len(str(num)) == len(str_a):
            return num
            
# Read input
a = int(input().strip())
b = int(input().strip())

# Get result and print
result = max_permutation_not_exceeding(a, b)
print(result)