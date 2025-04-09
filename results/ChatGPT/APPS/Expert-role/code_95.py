def generate_string(n, s, t):
    # Create the base string with n 'a's, n 'b's, and n 'c's
    base_string = 'a' * n + 'b' * n + 'c' * n
    
    # Check if it's possible to form a valid string
    if s[0] == t[0] or s[0] == t[1] or s[1] == t[0] or s[1] == t[1]:
        print("NO")
        return
    
    # Initialize the result list
    res = []

    # Create a list of characters to work with
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    
    # Current characters to be added
    current = 0
    
    while current < len(chars):
        # Try to add a character while avoiding the substrings s and t
        for i in range(current, len(chars)):
            # Check the last two added characters
            if len(res) >= 1 and chars[i] == res[-1]:
                continue
            if len(res) >= 2 and (res[-1] == s[0] and res[-2] == s[1]) or (res[-1] == t[0] and res[-2] == t[1]):
                continue
            
            # Add the character to the result
            res.append(chars[i])
            # Move the current pointer
            current += 1
            break
        else:
            # If we can't add any character, break the loop
            break
            
    # If we filled the result with the necessary length
    if len(res) == 3 * n:
        print("YES")
        print(''.join(res))
    else:
        print("NO")

# Read input
n = int(input())
s = input().strip()
t = input().strip()

# Generate the string
generate_string(n, s, t)