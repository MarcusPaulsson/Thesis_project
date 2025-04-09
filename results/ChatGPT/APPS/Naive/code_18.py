def lexicographically_minimal_string(s):
    t = []
    u = []
    
    for char in s:
        t.append(char)
        while t and (not u or t[-1] <= u[-1]):
            u.append(t.pop())
    
    return ''.join(u)

# Read input
s = input().strip()
# Get the result
result = lexicographically_minimal_string(s)
# Print the output
print(result)