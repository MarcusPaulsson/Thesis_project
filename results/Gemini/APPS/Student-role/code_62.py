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
    
    start_nodes = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in adj and len(adj[char]) <= 1:
            start_nodes.append(char)
    
    
    used = set()
    layout = ""
    
    if not start_nodes:
        if len(adj) > 0:
            
            start_char = next(iter(adj))
            start_nodes.append(start_char)
        else:
            layout = "abcdefghijklmnopqrstuvwxyz"
            print("YES")
            print(layout)
            return
    
    
    for start_node in start_nodes:
        
        
        temp_layout = ""
        temp_used = set()
        
        curr = start_node
        
        while curr is not None and curr not in temp_used:
            temp_layout += curr
            temp_used.add(curr)
            
            next_node = None
            if curr in adj:
                for neighbor in adj[curr]:
                    if neighbor not in temp_used:
                        next_node = neighbor
                        break
            
            curr = next_node
            
        if len(temp_layout) == len(adj):
            layout = temp_layout
            used = temp_used
            break

    if len(layout) == 0:
        print("NO")
        return

    for char in adj:
        if char not in layout:
            print("NO")
            return
    
    
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in adj:
            layout += char

    if len(layout) != 26:
        print("NO")
        return

    print("YES")
    print(layout)

t = int(input())
for _ in range(t):
    solve()