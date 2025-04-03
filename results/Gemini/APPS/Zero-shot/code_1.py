def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    def get_path(start, end):
        q = [(start, [start])]
        visited = set()
        while q:
            node, path = q.pop(0)
            if node == end:
                return path
            visited.add(node)
            for u, v in edges:
                neighbor = None
                if u == node and v not in visited:
                    neighbor = v
                elif v == node and u not in visited:
                    neighbor = u
                if neighbor:
                    q.append((neighbor, path + [neighbor]))
        return None

    def count_edges(a, b, c):
        path_ab = get_path(a, b)
        path_bc = get_path(b, c)
        path_ac = get_path(a, c)
        
        edges_ab = set()
        for i in range(len(path_ab) - 1):
            u, v = sorted((path_ab[i], path_ab[i+1]))
            edges_ab.add((u, v))

        edges_bc = set()
        for i in range(len(path_bc) - 1):
            u, v = sorted((path_bc[i], path_bc[i+1]))
            edges_bc.add((u, v))

        edges_ac = set()
        for i in range(len(path_ac) - 1):
            u, v = sorted((path_ac[i], path_ac[i+1]))
            edges_ac.add((u, v))

        all_edges = edges_ab.union(edges_bc).union(edges_ac)
        return len(all_edges)

    best_count = -1
    best_a, best_b, best_c = -1, -1, -1

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            for c in range(1, n + 1):
                if a == c or b == c:
                    continue
                
                count = count_edges(a, b, c)
                if count > best_count:
                    best_count = count
                    best_a, best_b, best_c = a, b, c

    print(best_count)
    print(best_a, best_b, best_c)

solve()