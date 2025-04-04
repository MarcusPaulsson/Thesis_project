def lexicographically_minimal_string(s):
    t = []
    u = []
    for char in s:
        while t and char < t[-1]:
            u.append(t.pop())
        t.append(char)
    while t:
        u.append(t.pop())
    return ''.join(u)

s = input().strip()
print(lexicographically_minimal_string(s))