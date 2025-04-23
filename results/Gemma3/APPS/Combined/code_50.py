def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def get_path(start, end):
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
    
    max_edges = 0
    best_a, best_b, best_c = -1, -1, -1
    
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            for c in range(1, n + 1):
                if a == c or b == c:
                    continue
                
                path_ab = get_path(a, b)
                path_bc = get_path(b, c)
                path_ac = get_path(a, c)
                
                if path_ab is None or path_bc is None or path_ac is None:
                    continue
                
                all_edges = set()
                for i in range(len(path_ab) - 1):
                    all_edges.add(tuple(sorted((path_ab[i], path_ab[i+1]))))
                for i in range(len(path_bc) - 1):
                    all_edges.add(tuple(sorted((path_bc[i], path_bc[i+1]))))
                for i in range(len(path_ac) - 1):
                    all_edges.add(tuple(sorted((path_ac[i], path_ac[i+1]))))
                
                if len(all_edges) > max_edges:
                    max_edges = len(all_edges)
                    best_a, best_b, best_c = a, b, c
    
    print(max_edges)
    print(best_a, best_b, best_c)

solve()