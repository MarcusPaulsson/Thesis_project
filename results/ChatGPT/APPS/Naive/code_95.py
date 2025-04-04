def generate_string(n, s, t):
    # Create a string containing n 'a's, n 'b's, and n 'c's
    chars = 'a' * n + 'b' * n + 'c' * n
    
    # Check if we can create a valid string
    for i in range(len(chars) - 1):
        if chars[i:i + 2] == s or chars[i:i + 2] == t:
            # If we find s or t, we need to rearrange
            chars = list(chars)  # Convert to a list to manipulate
            # Swap the last two characters to avoid the substring
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
            break
    else:
        # If we never found a conflict, just return the string
        return ''.join(chars)
    
    # Check the string again for the presence of s and t
    if s in ''.join(chars) or t in ''.join(chars):
        return "NO"
    
    return "YES\n" + ''.join(chars)

# Read input
n = int(input().strip())
s = input().strip()
t = input().strip()

# Generate and print the result
result = generate_string(n, s, t)
print(result)