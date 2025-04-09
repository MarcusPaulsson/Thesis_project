from itertools import permutations

def max_permutation(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Generate all unique permutations of the digits of a
    perm_set = set(permutations(a_str))
    
    max_num = -1
    for perm in perm_set:
        # Join the permutation tuple to form a string, then convert to integer
        num = int(''.join(perm))
        
        # Check if the number is valid: less than or equal to b and same length as a
        if num <= b and len(str(num)) == len(a_str) and str(num)[0] != '0':
            max_num = max(max_num, num)
    
    return max_num

# Input
a = int(input().strip())
b = int(input().strip())

# Output
print(max_permutation(a, b))