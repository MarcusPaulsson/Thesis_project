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

    import itertools
    for i in range(1 << m):
        tree_edges = []
        for j in range(m):
            if (i >> j) & 1:
                tree_edges.append(edges[j])

        if len(tree_edges) != n - 1:
            continue
        
        import collections
        adj = collections.defaultdict(list)
        for u, v in tree_edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def is_connected(tree_edges, n):
            if not tree_edges:
                return n == 1
            
            visited = set()
            q = collections.deque([tree_edges[0][0]])
            visited.add(tree_edges[0][0])
            
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            
            return len(visited) == n

        if is_connected(tree_edges, n) and check_degree(tree_edges) == d:
            print("YES")
            for u, v in tree_edges:
                print(u, v)
            return

    print("NO")

solve()