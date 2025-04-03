def solve():
    n = int(input())
    s = list(input())
    t = list(input())
    
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        counts[char] = counts.get(char, 0) + 1
    
    for char in counts:
        if counts[char] % 2 != 0:
            print("No")
            return
    
    swaps = []
    for i in range(n):
        if s[i] != t[i]:
            found = False
            for j in range(i + 1, n):
                if s[j] == s[i]:
                    swaps.append((j + 1, i + 1))
                    s[j], t[i] = t[i], s[j]
                    found = True
                    break
            if not found:
                for j in range(i + 1, n):
                    if t[j] == s[i]:
                        swaps.append((i + 1, j + 1))
                        s[i], t[j] = t[j], s[i]
                        swaps.append((j + 1, i + 1))
                        s[j], t[i] = t[i], s[j]
                        break
    
    print("Yes")
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

k = int(input())
for _ in range(k):
    solve()