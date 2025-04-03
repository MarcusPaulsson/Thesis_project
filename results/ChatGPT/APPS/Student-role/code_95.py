def generate_string(n, s, t):
    # Create a base string with n 'a's, n 'b's, and n 'c's
    base_string = 'a' * n + 'b' * n + 'c' * n
    # Check for forbidden substrings and try to rearrange
    from itertools import permutations

    # Generate all permutations of the base string
    for perm in set(permutations(base_string)):
        candidate = ''.join(perm)
        if s not in candidate and t not in candidate:
            return "YES\n" + candidate
            
    return "NO"

# Read input
n = int(input())
s = input().strip()
t = input().strip()

# Generate and print result
result = generate_string(n, s, t)
print(result)