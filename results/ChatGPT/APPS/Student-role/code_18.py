def minimal_lexicographic_u(s):
    t = []
    u = []
    
    for char in s:
        t.append(char)
        while t and (not u or t[-1] <= u[-1]):
            u.append(t.pop())
    
    return ''.join(u)

# Input
s = input().strip()
# Output
print(minimal_lexicographic_u(s))