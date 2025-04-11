n = int(input())
s = input().strip()
t = input().strip()

# Create a list of characters to use
chars = ['a'] * n + ['b'] * n + ['c'] * n

# Function to check if the current string contains forbidden substrings
def contains_forbidden_substrings(res):
    return s in res or t in res

# Generate a valid string without forbidden substrings
def generate_valid_string(n, s, t):
    # Start with a base pattern that avoids the forbidden substrings
    base = "abc" * n
    # Check if the base contains forbidden substrings
    if contains_forbidden_substrings(base):
        # If it does, we can try to rearrange
        # We can use a simple strategy to avoid forbidden pairs
        # by cycling through the characters
        res = []
        for i in range(n):
            if i % 2 == 0:
                res.append('a')
                res.append('b')
                res.append('c')
            else:
                res.append('c')
                res.append('a')
                res.append('b')
        res = ''.join(res)
        if contains_forbidden_substrings(res):
            return "NO"
        return res
    return base

result = generate_valid_string(n, s, t)
if result == "NO":
    print("NO")
else:
    print("YES")
    print(result)