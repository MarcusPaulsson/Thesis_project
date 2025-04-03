def solve():
    n = int(input())
    s = list(input())
    t = list(input())

    ops = []
    
    for i in range(n):
        if s[i] != t[i]:
            found = False
            for j in range(i + 1, n):
                if s[j] == s[i]:
                    ops.append((j + 1, i + 1))
                    s[j], t[i] = t[i], s[j]
                    found = True
                    break
            if not found:
                for j in range(i + 1, n):
                    if t[j] == s[i]:
                        ops.append((i + 1, j + 1))
                        s[i], t[j] = t[j], s[i]
                        ops.append((j + 1, i + 1))
                        s[j], t[i] = t[i], s[j]
                        found = True
                        break
            if not found:
                print("No")
                return
    
    if len(ops) <= 2 * n:
        print("Yes")
        print(len(ops))
        for i, j in ops:
            print(i, j)
    else:
        print("No")

k = int(input())
for _ in range(k):
    solve()