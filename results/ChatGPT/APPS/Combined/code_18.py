def lexicographically_minimal_string(s: str) -> str:
    t = []
    u = []
    
    for char in s:
        t.append(char)
        
        while t and (not s or t[-1] <= s[0]):
            u.append(t.pop())
        
        if s:
            s = s[1:]
    
    while t:
        u.append(t.pop())
    
    return ''.join(u)

# Example usage
s = input().strip()
print(lexicographically_minimal_string(s))