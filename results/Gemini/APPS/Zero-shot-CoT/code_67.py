def solve():
    n = int(input())
    s = list(input())
    t = list(input())

    ops = []
    for i in range(n):
        if s[i] == t[i]:
            continue
        
        found = False
        for j in range(i + 1, n):
            if s[i] == s[j]:
                ops.append((j + 1, i + 1))
                s[j], t[i] = t[i], s[j]
                found = True
                break
        
        if found:
            continue
        
        for j in range(i + 1, n):
            if s[i] == t[j]:
                ops.append((i + 1, j + 1))
                s[i], t[j] = t[j], s[i]
                
                ops.append((j + 1, j + 1))
                s[j], t[j] = t[j], s[j]
                found = True
                break
        
        if not found:
            print("No")
            return
    
    print("Yes")
    print(len(ops))
    for op in ops:
        print(op[0], op[1])

k = int(input())
for _ in range(k):
    solve()