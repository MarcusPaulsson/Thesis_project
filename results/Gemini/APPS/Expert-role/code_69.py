def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    def find_spanning_tree(graph_edges, num_nodes, required_degree):
        adj = [[] for _ in range(num_nodes + 1)]
        for u, v in graph_edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start_node, all_edges):
            visited = [False] * (num_nodes + 1)
            q = [start_node]
            visited[start_node] = True
            spanning_tree_edges = []
            
            while q:
                u = q.pop(0)
                for v in adj[u]:
                    if not visited[v]:
                        edge = (min(u, v), max(u, v))
                        if edge in [tuple(sorted(e)) for e in graph_edges]:
                                spanning_tree_edges.append((u, v))
                                visited[v] = True
                                q.append(v)
            
            for i in range(1, num_nodes + 1):
                if not visited[i]:
                    return None
            return spanning_tree_edges

        spanning_tree = bfs(1, edges)

        if spanning_tree is None:
            return None

        degree_of_one = 0
        for u, v in spanning_tree:
            if u == 1 or v == 1:
                degree_of_one += 1

        if degree_of_one == required_degree:
            return spanning_tree
        else:
            return None
        

    result = find_spanning_tree(edges, n, d)

    if result:
        print("YES")
        for u, v in result:
            print(u, v)
    else:
        print("NO")

solve()