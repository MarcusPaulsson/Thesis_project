def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    def get_path(start, end, adj):
        q = [(start, [start])]
        visited = {start}
        while q:
            node, path = q.pop(0)
            if node == end:
                return path
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, path + [neighbor]))
        return None

    def get_edges_from_path(path):
        edges_in_path = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            edges_in_path.append(tuple(sorted((u, v))))
        return edges_in_path
    
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    best_count = -1
    best_a = -1
    best_b = -1
    best_c = -1

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

                edges_ab = get_edges_from_path(path_ab)
                edges_bc = get_edges_from_path(path_bc)
                edges_ac = get_edges_from_path(path_ac)

                all_edges = set(edges_ab + edges_bc + edges_ac)
                
                if len(all_edges) > best_count:
                    best_count = len(all_edges)
                    best_a = a
                    best_b = b
                    best_c = c
    
    print(best_count)
    print(best_a, best_b, best_c)

solve()