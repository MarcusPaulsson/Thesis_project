def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    def build_spanning_tree(edges, n, d):
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start_node, edges_to_use):
            visited = [False] * (n + 1)
            q = [start_node]
            visited[start_node] = True
            spanning_tree_edges = []
            
            while q:
                u = q.pop(0)
                for v in adj[u]:
                    if not visited[v]:
                        edge = (min(u, v), max(u, v))
                        if edge in edges_to_use:
                            visited[v] = True
                            q.append(v)
                            spanning_tree_edges.append((u, v))
            
            all_visited = all(visited[1:])
            if all_visited:
                return spanning_tree_edges
            else:
                return None

        
        import itertools
        
        for comb in itertools.combinations(edges, n - 1):
            
            spanning_tree_edges = bfs(1, set(comb))
            
            if spanning_tree_edges:
                degree_one = 0
                for u, v in spanning_tree_edges:
                    if u == 1 or v == 1:
                        degree_one += 1
                
                if degree_one == d:
                    return spanning_tree_edges
        
        return None

    spanning_tree = build_spanning_tree(edges, n, d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

solve()