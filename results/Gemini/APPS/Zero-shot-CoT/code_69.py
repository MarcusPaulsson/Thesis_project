def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    def check_degree(tree):
        degree = 0
        for u, v in tree:
            if u == 1 or v == 1:
                degree += 1
        return degree

    def is_connected(tree, num_nodes):
        if not tree:
            return False if num_nodes > 1 else True
        
        adj = [[] for _ in range(num_nodes + 1)]
        for u, v in tree:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * (num_nodes + 1)
        
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        dfs(1)
        
        for i in range(1, num_nodes + 1):
            if not visited[i]:
                return False
        return True

    import itertools
    
    for i in itertools.combinations(edges, n - 1):
        tree = list(i)
        if is_connected(tree, n) and check_degree(tree) == d:
            print("YES")
            for u, v in tree:
                print(u, v)
            return

    print("NO")

solve()