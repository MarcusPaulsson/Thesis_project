def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    def get_path(start, end, adj):
        q = [(start, [start])]
        while q:
            node, path = q.pop(0)
            if node == end:
                return path
            for neighbor in adj[node]:
                if neighbor not in path:
                    q.append((neighbor, path + [neighbor]))
        return None

    def edges_in_path(path):
        edge_set = set()
        for i in range(len(path) - 1):
            u, v = sorted((path[i], path[i+1]))
            edge_set.add((u, v))
        return edge_set
    
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    best_count = -1
    best_a, best_b, best_c = -1, -1, -1

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            for c in range(1, n + 1):
                if a == c or b == c:
                    continue

                path_ab = get_path(a, b, adj)
                path_bc = get_path(b, c, adj)
                path_ac = get_path(a, c, adj)
                
                if path_ab is None or path_bc is None or path_ac is None:
                    continue

                edges_ab = edges_in_path(path_ab)
                edges_bc = edges_in_path(path_bc)
                edges_ac = edges_in_path(path_ac)

                union_edges = edges_ab.union(edges_bc).union(edges_ac)
                
                count = len(union_edges)

                if count > best_count:
                    best_count = count
                    best_a, best_b, best_c = a, b, c

    print(best_count)
    print(best_a, best_b, best_c)

solve()