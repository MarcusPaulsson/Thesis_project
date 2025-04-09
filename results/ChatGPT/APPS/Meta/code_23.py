def max_permutation_not_exceeding(a: int, b: int) -> int:
    from itertools import permutations
    
    # Convert 'a' to a string and generate all unique permutations
    str_a = str(a)
    digits = sorted(str_a, reverse=True)  # Sort digits in descending order for maximum number
    max_length = len(str_a)
    
    # Function to check if a number is valid (not exceeding b and has no leading zero)
    def is_valid(num_str):
        return num_str[0] != '0' and int(num_str) <= b
    
    # Generate permutations and filter out invalid ones
    for perm in permutations(digits):
        candidate = ''.join(perm)
        if len(candidate) == max_length and is_valid(candidate):
            return int(candidate)  # Return the first valid permutation found (which is the largest due to sorting)
    
    return a  # If no valid permutation found, return 'a' as a fallback (guaranteed to exist)

# Read input values
a = int(input())
b = int(input())

# Call the function and print the result
result = max_permutation_not_exceeding(a, b)
print(result)