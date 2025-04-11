def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    def check(tree_edges):
        adj = [[] for _ in range(n + 1)]
        for u, v in tree_edges:
            adj[u].append(v)
            adj[v].append(u)
        
        degree_one = len(adj[1])
        
        if degree_one != d:
            return False

        visited = [False] * (n + 1)
        q = [1]
        visited[1] = True
        count = 0
        while q:
            u = q.pop(0)
            count += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        return count == n

    import itertools
    for i in itertools.combinations(edges, n - 1):
        if check(i):
            print("YES")
            for u, v in i:
                print(u, v)
            return
    print("NO")

solve()