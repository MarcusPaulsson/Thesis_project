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

    def find_spanning_tree(edges, n, d):
        import itertools
        for r in range(n, len(edges) + 1):
            for combination in itertools.combinations(edges, n - 1):
                
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
                for u, v in combination:
                    if union(u, v):
                        num_edges += 1
                
                if num_edges == n - 1:
                    if check_degree(combination) == d:
                        return combination
        return None

    spanning_tree = find_spanning_tree(edges, n, d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

solve()