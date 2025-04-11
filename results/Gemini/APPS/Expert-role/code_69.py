def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    def find_spanning_tree(graph_edges, num_nodes, required_degree):
        adj = [[] for _ in range(num_nodes + 1)]
        for u, v in graph_edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start_node, available_edges):
            visited = {start_node}
            queue = [start_node]
            spanning_tree_edges = []

            while queue:
                u = queue.pop(0)
                neighbors = []
                for v1, v2 in available_edges:
                    if v1 == u:
                        neighbors.append(v2)
                    elif v2 == u:
                        neighbors.append(v1)
                
                for v in neighbors:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
                        spanning_tree_edges.append((u, v))
            
            if len(visited) == num_nodes:
                return spanning_tree_edges
            else:
                return None

        
        import itertools
        
        for comb in itertools.combinations(edges, n - 1):
            
            spanning_tree_edges = bfs(1, list(comb))
            
            if spanning_tree_edges is not None:
                degree_of_one = 0
                for u, v in spanning_tree_edges:
                    if u == 1 or v == 1:
                        degree_of_one += 1
                
                if degree_of_one == required_degree:
                    return spanning_tree_edges
        
        return None

    spanning_tree = find_spanning_tree(edges, n, d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

solve()