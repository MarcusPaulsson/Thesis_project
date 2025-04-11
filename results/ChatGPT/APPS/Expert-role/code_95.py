def generate_string(n, s, t):
    # Create a list of characters to use
    chars = ['a'] * n + ['b'] * n + ['c'] * n
    # Create a result list
    res = []
    
    # Function to check if the last two characters in res form a forbidden substring
    def is_forbidden():
        if len(res) < 2:
            return False
        return ''.join(res[-2:]) in (s, t)

    # Try to build the result string
    for _ in range(3 * n):
        for char in chars:
            res.append(char)
            if not is_forbidden():
                chars.remove(char)
                break
            res.pop()  # Remove the last character if it leads to forbidden substring

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