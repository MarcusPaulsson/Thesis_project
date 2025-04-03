def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    def build_graph(edge_list):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v in edge_list:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def is_connected(edge_list):
        if not edge_list:
            return False if n > 1 else True
        
        graph = build_graph(edge_list)
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(edge_list[0][0])
        return len(visited) == n

    def find_spanning_tree(edges, d):
        import itertools
        for i in itertools.combinations(edges, n - 1):
            spanning_tree_edges = list(i)
            if is_connected(spanning_tree_edges):
                degree = 0
                for u, v in spanning_tree_edges:
                    if u == 1 or v == 1:
                        degree += (u == 1) + (v == 1)
                
                degree = sum(1 for u, v in spanning_tree_edges if u == 1 or v == 1)
                
                count = 0
                for u, v in spanning_tree_edges:
                    if u == 1 or v == 1:
                        count+=1
                
                first_node_degree = 0
                graph = build_graph(spanning_tree_edges)
                first_node_degree = len(graph[1])
                
                if first_node_degree == d:
                    return spanning_tree_edges
        return None

    spanning_tree = find_spanning_tree(edges, d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")
solve()