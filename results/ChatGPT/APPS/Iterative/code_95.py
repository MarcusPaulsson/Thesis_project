n = int(input())
s = input().strip()
t = input().strip()

# Create the resulting string with n 'a's, n 'b's, and n 'c's
res = ['a'] * n + ['b'] * n + ['c'] * n

# Function to check if the substrings s or t are present
def contains_substrings(res, s, t):
    result_str = ''.join(res)
    return s in result_str or t in result_str

# Generate a valid string
def generate_valid_string(n, s, t):
    # Create a simple base pattern
    base_pattern = "abc" * n
    # Check if the basic pattern contains s or t
    if contains_substrings(base_pattern, s, t):
        # If it does, we can try a different arrangement
        # Attempt to create a pattern that avoids s and t
        res = []
        for i in range(n):
            res.append('a')
            res.append('b')
            res.append('c')
        
        # Convert to string
        res_str = ''.join(res)
        if not contains_substrings(res_str, s, t):
            return res_str
    
    # If the basic pattern works, return it
    return base_pattern

result = generate_valid_string(n, s, t)

if result:
    print("YES")
    print(result)
else:
    print("NO")