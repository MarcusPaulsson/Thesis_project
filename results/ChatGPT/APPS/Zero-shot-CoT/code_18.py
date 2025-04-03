s = input().strip()
t = []
u = []

while s or t:
    if s:
        t.append(s[0])
        s = s[1:]
    
    while t:
        if not u or t[-1] <= u[-1]:
            u.append(t.pop())
        else:
            break

print(''.join(u))