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
        edges_on_path = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            edges_on_path.append(tuple(sorted((u, v))))
        return edges_on_path
    
    best_count = -1
    best_a, best_b, best_c = -1, -1, -1

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            for c in range(1, n + 1):
                if a == c or b == c:
                    continue

                adj = {i: [] for i in range(1, n + 1)}
                for u, v in edges:
                    adj[u].append(v)
                    adj[v].append(u)

                path_ab = get_path(a, b, adj)
                path_bc = get_path(b, c, adj)
                path_ac = get_path(a, c, adj)
                
                edges_ab = edges_in_path(path_ab) if path_ab else []
                edges_bc = edges_in_path(path_bc) if path_bc else []
                edges_ac = edges_in_path(path_ac) if path_ac else []

                all_edges = set(edges_ab + edges_bc + edges_ac)
                
                if len(all_edges) > best_count:
                    best_count = len(all_edges)
                    best_a, best_b, best_c = a, b, c

    print(best_count)
    print(best_a, best_b, best_c)

solve()