def lexicographically_minimal_string(s):
    t = []
    u = []
    
    for char in s:
        t.append(char)
        # Maintain the order of characters in t for forming u
        while t and (not u or t[-1] <= u[-1]):
            u.append(t.pop())
    
    # If there are still characters left in t after processing s
    while t:
        u.append(t.pop())
    
    # Join the list to form the final string
    return ''.join(u)

# Input
s = input().strip()
# Output the result
print(lexicographically_minimal_string(s))