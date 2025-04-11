def generate_string(n, s, t):
    # Create the base string with n 'a's, n 'b's, and n 'c's
    base = 'a' * n + 'b' * n + 'c' * n
    
    # Check if the forbidden substrings are present
    if s in base or t in base:
        return "NO"
    
    # Try to construct a valid string
    from itertools import permutations
    
    # Generate all permutations of the base string
    for perm in set(permutations(base)):
        res = ''.join(perm)
        if s not in res and t not in res:
            return "YES\n" + res
    
    return "NO"

# Input reading
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate the result
result = generate_string(n, s, t)
print(result)