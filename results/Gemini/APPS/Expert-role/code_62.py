def solve():
    s = input()
    adj = {}
    for i in range(len(s) - 1):
        a, b = s[i], s[i+1]
        if a not in adj:
            adj[a] = set()
        if b not in adj:
            adj[b] = set()
        adj[a].add(b)
        adj[b].add(a)
    
    for char in adj:
        if len(adj[char]) > 2:
            print("NO")
            return
    
    starts = []
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char in adj and len(adj[char]) <= 1:
            starts.append(char)
        elif char not in adj:
            starts.append(char)
    
    if not starts:
        print("NO")
        return
    
    visited = set()
    layout = ""
    
    for start in starts:
        if start not in visited:
            curr = start
            while curr is not None:
                if curr in visited:
                    print("NO")
                    return
                visited.add(curr)
                layout += curr
                
                next_char = None
                if curr in adj:
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            next_char = neighbor
                            break
                curr = next_char
    
    if len(layout) != 26:
        for char in "abcdefghijklmnopqrstuvwxyz":
            if char not in layout:
                layout += char
    
    if len(layout) != 26:
        print("NO")
        return
    
    print("YES")
    print(layout)

t = int(input())
for _ in range(t):
    solve()