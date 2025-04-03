def solve():
    n = int(input())
    s = list(input())
    t = list(input())

    ops = []
    for _ in range(2 * n):
        if s == t:
            break

        found = False
        for i in range(n):
            if s[i] != t[i]:
                for j in range(n):
                    if s[i] == t[j]:
                        ops.append((i + 1, j + 1))
                        s[i], t[j] = t[j], s[i]
                        found = True
                        break
                if found:
                    break
                
                for j in range(n):
                    if t[i] == s[j]:
                        ops.append((j + 1, i + 1))
                        s[j], t[i] = t[i], s[j]
                        found = True
                        break
                if found:
                    break
        
        if not found:
            break
    
    if s == t:
        print("Yes")
        print(len(ops))
        for i, j in ops:
            print(i, j)
    else:
        print("No")

k = int(input())
for _ in range(k):
    solve()