def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    def check_degree(tree):
        degree = 0
        for u, v in tree:
            if u == 1 or v == 1:
                degree += 1
        return degree

    import itertools
    for i in itertools.combinations(edges, n - 1):
        tree = list(i)
        
        parent = list(range(n + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
        
        num_edges = 0
        is_spanning = True
        for u, v in tree:
            if union(u, v):
                num_edges += 1
        
        for j in range(1, n+1):
            find(j)

        num_components = len(set(parent[1:]))
        if num_components > 1:
            is_spanning = False
        
        if is_spanning and check_degree(tree) == d:
            print("YES")
            for u, v in tree:
                print(u, v)
            return

    print("NO")

solve()