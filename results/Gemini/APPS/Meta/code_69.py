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

    def find_spanning_tree(target_degree):
        import itertools

        for i in range(n - 1, min(m + 1, n + 5)):
            for comb in itertools.combinations(edges, n - 1):
                
                
                adj = [[] for _ in range(n + 1)]
                for u, v in comb:
                    adj[u].append(v)
                    adj[v].append(u)

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

                if count == n:
                    if check_degree(comb) == target_degree:
                        return comb
        return None

    spanning_tree = find_spanning_tree(d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

solve()