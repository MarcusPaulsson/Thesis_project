def lexicographically_minimal_string(s):
    t = []
    u = []
    
    for char in s:
        t.append(char)
        while t:
            if len(u) == 0 or t[-1] <= u[-1]:
                u.append(t.pop())
            else:
                break
    
    return ''.join(u)

s = input().strip()
result = lexicographically_minimal_string(s)
print(result)