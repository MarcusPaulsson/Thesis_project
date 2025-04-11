def generate_string(n, s, t):
    # Create a list of characters to use
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    # Create a set of forbidden substrings
    forbidden = {s, t}
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden(res):
        return res[-2:] in forbidden
    
    # Result string
    res = []
    
    # Try to build the result string
    for char in chars:
        # If adding this character would create a forbidden substring, skip it
        if len(res) >= 1 and res[-1] == char:
            continue
        if len(res) >= 2 and is_forbidden(res + [char]):
            continue
        
        res.append(char)
    
    # If we have enough characters, return the result
    if len(res) == 3 * n:
        return "YES\n" + ''.join(res)
    else:
        return "NO"

# Read input
n = int(input())
s = input().strip()
t = input().strip()

# Generate the result
result = generate_string(n, s, t)
print(result)