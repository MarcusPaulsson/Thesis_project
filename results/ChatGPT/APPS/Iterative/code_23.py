from itertools import permutations

def max_permutation_not_exceeding(a, b):
    a_str = str(a)
    b_str = str(b)
    
    # Generate all unique permutations of the digits of a
    perm = sorted(set(permutations(a_str)), reverse=True)

    for p in perm:
        # Join the tuple of characters to form a number
        num_str = ''.join(p)
        # Skip permutations that lead with '0' or don't match the length of a
        if num_str[0] != '0' and len(num_str) == len(a_str):
            num = int(num_str)
            # Check if it is less than or equal to b
            if num <= b:
                return num

# Input reading
a = int(input().strip())
b = int(input().strip())

# Get and print the result
result = max_permutation_not_exceeding(a, b)
print(result)