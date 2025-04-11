def generate_string(n, s, t):
    # Create a list of characters to use in the result
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Function to check if the last two characters of the result form a forbidden substring
    def is_forbidden(res):
        return res[-2:] == s or res[-2:] == t
    
    # Initialize the result string
    res = []
    
    # Try to build the result string
    for char in chars:
        res.append(char)
        # If the last two characters form a forbidden substring, we need to adjust
        while len(res) >= 2 and is_forbidden(res):
            # Remove the last character and try to replace it with a different character
            last_char = res.pop()
            # Find a different character to replace it
            for replacement in ['a', 'b', 'c']:
                if replacement != last_char and (len(res) < 1 or res[-1] != replacement):
                    res.append(replacement)
                    break
            else:
                # If we can't find a valid replacement, return "NO"
                return "NO", ""
    
    return "YES", ''.join(res)

# Read input
n = int(input())
s = input().strip()
t = input().strip()

# Generate the string
result = generate_string(n, s, t)

# Print the result
print(result[0])
if result[0] == "YES":
    print(result[1])