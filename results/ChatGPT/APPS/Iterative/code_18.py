s = input().strip()
t = []
u = []

for char in s:
    t.append(char)
    while t and (not u or t[-1] <= u[-1]):
        u.append(t.pop())

# Append any remaining characters in t to u
while t:
    u.append(t.pop())

print(''.join(u))