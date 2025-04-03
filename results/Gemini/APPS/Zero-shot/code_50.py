def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    def get_path(start, end, graph):
        q = [(start, [start])]
        while q:
            node, path = q.pop(0)
            if node == end:
                return path
            for neighbor in graph[node]:
                if neighbor not in path:
                    q.append((neighbor, path + [neighbor]))
        return None

    def get_edges_from_path(path):
        edges_in_path = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            edges_in_path.append(tuple(sorted((u, v))))
        return edges_in_path

    def calculate_edges(a, b, c, graph):
        path_ab = get_path(a, b, graph)
        path_bc = get_path(b, c, graph)
        path_ac = get_path(a, c, graph)

        edges_ab = get_edges_from_path(path_ab)
        edges_bc = get_edges_from_path(path_bc)
        edges_ac = get_edges_from_path(path_ac)

        all_edges = set(edges_ab + edges_bc + edges_ac)
        return len(all_edges)

    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    best_count = -1
    best_a, best_b, best_c = -1, -1, -1

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            for c in range(1, n + 1):
                if a == c or b == c:
                    continue

                count = calculate_edges(a, b, c, graph)
                if count > best_count:
                    best_count = count
                    best_a, best_b, best_c = a, b, c

    print(best_count)
    print(best_a, best_b, best_c)

solve()