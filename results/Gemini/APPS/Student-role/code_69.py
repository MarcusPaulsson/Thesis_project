def solve():
    a, b = map(int, input().split())
    s = input()
    n = len(s)
    
    groups = []
    i = 0
    while i < n:
        if s[i] == '1':
            j = i
            while j < n and s[j] == '1':
                j += 1
            groups.append((i, j - 1))
            i = j
        else:
            i += 1
            
    if not groups:
        print(0)
        return
    
    cost = a * len(groups)
    
    for i in range(len(groups) - 1):
        dist = groups[i+1][0] - groups[i][1] - 1
        cost -= min(a, b * dist)
        
    print(cost)

t = int(input())
for _ in range(t):
    solve()