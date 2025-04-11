def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    def check_degree(tree_edges):
        degree = 0
        for u, v in tree_edges:
            if u == 1 or v == 1:
                degree += 1
        return degree

    def is_connected(tree_edges, n):
        if not tree_edges:
            return False
        
        adj = {i: [] for i in range(1, n + 1)}
        for u, v in tree_edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = [1]
        visited.add(1)

        while q:
            u = q.pop(0)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        
        return len(visited) == n

    def find_spanning_tree(edges, n, d):
        from itertools import combinations

        for comb in combinations(edges, n - 1):
            tree_edges = list(comb)
            if is_connected(tree_edges, n) and check_degree(tree_edges) == d:
                return tree_edges
        return None

    spanning_tree = find_spanning_tree(edges, n, d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

solve()