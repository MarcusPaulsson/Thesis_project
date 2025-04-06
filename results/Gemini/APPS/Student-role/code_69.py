def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    def check_degree(tree_edges):
        degree = 0
        for u, v in tree_edges:
            if u == 1 or v == 1:
                degree += 1
        return degree
    
    def is_connected(tree_edges):
        if not tree_edges:
            return False
        
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
            
        for u, v in tree_edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * (n + 1)
        q = [1]
        visited[1] = True
        
        while q:
            u = q.pop(0)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        for i in range(1, n + 1):
            if not visited[i]:
                return False
        return True

    
    def find_spanning_tree(index, current_tree):
        if len(current_tree) == n - 1:
            if is_connected(current_tree) and check_degree(current_tree) == d:
                return current_tree
            else:
                return None
        
        if index == m:
            return None
        
        # Exclude the current edge
        result = find_spanning_tree(index + 1, current_tree)
        if result:
            return result
        
        # Include the current edge
        new_tree = current_tree + [edges[index]]
        result = find_spanning_tree(index + 1, new_tree)
        if result:
            return result
        
        return None
    
    spanning_tree = find_spanning_tree(0, [])
    
    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")
        

solve()