def generate_string(n, s, t):
    # Create the initial string with n 'a's, n 'b's, and n 'c's
    res = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Check pairs of characters to avoid forbidden substrings
    forbidden = {s, t}
    
    # We will attempt to build a valid string
    from itertools import permutations
    
    # Generate all permutations of the initial string
    for perm in permutations(res):
        candidate = ''.join(perm)
        if all(sub not in candidate for sub in forbidden):
            return "YES\n" + candidate
            
    return "NO"

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

# Generate the string
result = generate_string(n, s, t)
print(result)