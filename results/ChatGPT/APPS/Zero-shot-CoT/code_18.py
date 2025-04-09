def lexicographically_minimal_u(s):
    t = []
    u = []
    
    for char in s:
        # Push the character from s to t
        t.append(char)
        # Try to move characters from t to u in lexicographical order
        while t and (not u or t[-1] <= u[-1]):
            u.append(t.pop())
    
    # In case there are still characters in t, continue moving to u
    while t:
        u.append(t.pop())
    
    return ''.join(u)

# Read input
s = input().strip()
# Get the result
result = lexicographically_minimal_u(s)
# Print the result
print(result)