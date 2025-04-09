def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    def is_spanning_tree(tree_edges):
        if len(tree_edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n + 1)]
        for u, v in tree_edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * (n + 1)
        q = [1]
        visited[1] = True
        count = 0
        
        while q:
            u = q.pop(0)
            count += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        return count == n
    
    def get_degree(tree_edges, vertex):
        degree = 0
        for u, v in tree_edges:
            if u == vertex or v == vertex:
                degree += 1
        return degree
    
    import itertools
    
    for i in range(1 << m):
        tree_edges = []
        for j in range(m):
            if (i >> j) & 1:
                tree_edges.append(edges[j])
        
        if is_spanning_tree(tree_edges):
            if get_degree(tree_edges, 1) == d:
                print("YES")
                for u, v in tree_edges:
                    print(u, v)
                return
    
    print("NO")

solve()