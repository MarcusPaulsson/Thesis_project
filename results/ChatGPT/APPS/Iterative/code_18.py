def minimal_lexicographic_string(s):
    t = []
    u = []
    
    for char in s:
        t.append(char)
        while t:
            if not u or t[-1] <= u[-1]:
                u.append(t.pop())
            else:
                break
    
    return ''.join(u)

s = input().strip()
print(minimal_lexicographic_string(s))