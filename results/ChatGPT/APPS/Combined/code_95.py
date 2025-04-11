def generate_string(n, s, t):
    # Count of each character
    counts = {'a': n, 'b': n, 'c': n}
    
    # Create a list to hold the result
    res = []
    
    # Function to check if adding a character would create a forbidden substring
    def can_add_char(c):
        if len(res) >= 1 and res[-1] == c:
            return False
        if len(res) >= 1 and res[-1] + c in (s, t):
            return False
        return True
    
    # Try to build the result string
    while sum(counts.values()) > 0:
        for char in 'abc':
            if counts[char] > 0 and can_add_char(char):
                res.append(char)
                counts[char] -= 1
                break
        else:
            # If we went through all characters and couldn't add any, we are stuck
            return "NO"
    
    # Join the result list into a string
    result_string = ''.join(res)
    
    # Check if the result contains forbidden substrings
    if s in result_string or t in result_string:
        return "NO"
    
    return "YES\n" + result_string

# Input reading
n = int(input())
s = input().strip()
t = input().strip()

# Generate and print the result
print(generate_string(n, s, t))