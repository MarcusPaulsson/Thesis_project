def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    if len([neighbor for neighbor in adj[1]]) < d or d < 1:
        print("NO")
        return

    parent = [0] * (n + 1)
    degree_1 = 0
    spanning_tree = []
    visited = [False] * (n + 1)

    def dfs(u):
        nonlocal degree_1
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                if u == 1:
                    degree_1 += 1
                spanning_tree.append((u, v))
                dfs(v)

    dfs(1)

    if degree_1 > d:
        print("NO")
        return

    count = 0
    for i in range(1, n + 1):
        if visited[i]:
            count += 1
    
    if count != n:
        print("NO")
        return

    
    extra_edges = []
    for u, v in edges:
        if (u, v) not in spanning_tree and (v, u) not in spanning_tree:
            extra_edges.append((u, v))

    
    final_spanning_tree = []
    final_degree_1 = 0
    
    final_edges_set = set()

    for u, v in spanning_tree:
        if (u == 1 or v == 1):
            final_degree_1 += 1
        final_edges_set.add(tuple(sorted((u, v))))
    
    
    
    if final_degree_1 < d:
        
        possible = False
        for u, v in extra_edges:
            if u == 1 or v == 1:
                
                final_edges_set.add(tuple(sorted((u,v))))
                final_degree_1 += 1
                if final_degree_1 == d:
                    possible = True
                    break
                
        if not possible:
            print("NO")
            return
    
    if final_degree_1 > d:
        print("NO")
        return
    
    print("YES")
    for u, v in edges:
        if tuple(sorted((u, v))) in final_edges_set:
            final_spanning_tree.append((u, v))
            
    
    if len(final_spanning_tree) != n - 1:
        
        final_spanning_tree = []
        final_degree_1 = 0
        
        
        
        visited = [False] * (n + 1)

        parent = [0] * (n + 1)
        spanning_tree = []
        
        def dfs2(u):
            nonlocal degree_1
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    if u == 1:
                        degree_1 += 1
                    spanning_tree.append((u, v))
                    dfs2(v)

        degree_1 = 0
        dfs2(1)
        
        
        valid = True
        if degree_1 > d:
            valid = False
        
        count = 0
        for i in range(1, n + 1):
            if visited[i]:
                count += 1
        
        if count != n:
            valid = False
        
        
        if not valid:
            print("NO")
            return
        
        
        
        
        
        
        
        final_edges_set = set()

        for u, v in spanning_tree:
            if (u == 1 or v == 1):
                final_degree_1 += 1
            final_edges_set.add(tuple(sorted((u, v))))
        
        
        if final_degree_1 < d:
            
            possible = False
            for u, v in extra_edges:
                if u == 1 or v == 1:
                    
                    
                    if tuple(sorted((u,v))) not in final_edges_set:
                        
                        
                        
                        final_edges_set.add(tuple(sorted((u,v))))
                        final_degree_1 += 1
                        if final_degree_1 == d:
                            possible = True
                            break
                
            if not possible:
                print("NO")
                return
            
        if final_degree_1 > d:
            print("NO")
            return
        
        
        for u, v in edges:
            if tuple(sorted((u, v))) in final_edges_set:
                final_spanning_tree.append((u, v))
                
    
    for u, v in final_spanning_tree:
        print(u, v)

solve()