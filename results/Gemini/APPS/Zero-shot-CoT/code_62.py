def solve():
    s = input()
    adj = {}
    for char in s:
        adj[char] = set()
    
    for i in range(len(s) - 1):
        adj[s[i]].add(s[i+1])
        adj[s[i+1]].add(s[i])
    
    for char in adj:
        if len(adj[char]) > 2:
            print("NO")
            return
    
    used = set()
    layout = ""
    
    for char in s:
        if char not in used:
            start = char
            break
    else:
        print("YES")
        print("abcdefghijklmnopqrstuvwxyz")
        return
    
    curr = start
    used.add(curr)
    layout += curr
    
    while True:
        next_char = None
        for neighbor in adj[curr]:
            if neighbor not in used:
                next_char = neighbor
                break
        
        if next_char is None:
            break
        
        curr = next_char
        used.add(curr)
        layout += curr
    
    remaining = ""
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in used:
            remaining += char
    
    layout += remaining
    
    if len(layout) != 26:
        print("NO")
    else:
        print("YES")
        print(layout)

t = int(input())
for _ in range(t):
    solve()