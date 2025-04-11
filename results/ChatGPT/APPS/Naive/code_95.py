def generate_string(n, s, t):
    # Create a list of characters with n 'a', n 'b', and n 'c'
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Function to check if the last two characters form a forbidden substring
    def is_forbidden(res):
        return res[-2:] == s or res[-2:] == t
    
    # Resultant string
    res = []
    
    # Try to build the result string
    for char in chars:
        # If adding the current character would create a forbidden substring
        while res and is_forbidden(res + [char]):
            # If we can't add this character, we need to try the next available character
            if char == 'a':
                if n > 0:
                    char = 'b'
                elif n > 0:
                    char = 'c'
                else:
                    break
            elif char == 'b':
                if n > 0:
                    char = 'a'
                elif n > 0:
                    char = 'c'
                else:
                    break
            elif char == 'c':
                if n > 0:
                    char = 'a'
                elif n > 0:
                    char = 'b'
                else:
                    break
        
        # If we can add the character, do so
        if not is_forbidden(res + [char]):
            res.append(char)
    
    # Check if we have a valid result
    if len(res) == 3 * n:
        return "YES", ''.join(res)
    else:
        return "NO", ""

# Input reading
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate the string
result = generate_string(n, s, t)

# Output the result
print(result[0])
if result[0] == "YES":
    print(result[1])