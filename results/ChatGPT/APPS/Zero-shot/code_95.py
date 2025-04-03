def generate_string(n, s, t):
    # Create a list of the characters we need
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Check for impossible cases
    if (s[0] == t[0] and s[1] == t[1]) or (s[0] == t[1] and s[1] == t[0]):
        return "NO"
    
    # Attempt to create the result string
    from itertools import permutations
    
    for perm in permutations(chars):
        res = ''.join(perm)
        if s not in res and t not in res:
            return f"YES\n{res}"
    
    return "NO"

n = int(input().strip())
s = input().strip()
t = input().strip()

result = generate_string(n, s, t)
print(result)