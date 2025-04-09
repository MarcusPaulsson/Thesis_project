def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    def check_degree(tree_edges, degree):
        count = 0
        for u, v in tree_edges:
            if u == 1 or v == 1:
                count += 1
        return count == degree

    def find_spanning_tree(edges, n, d):
        import itertools
        for i in range(1 << len(edges)):
            tree_edges = []
            for j in range(len(edges)):
                if (i >> j) & 1:
                    tree_edges.append(edges[j])

            if len(tree_edges) != n - 1:
                continue

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
            for u, v in tree_edges:
                if union(u, v):
                    num_edges += 1
            
            is_connected = True
            root = find(1)
            for k in range(2, n + 1):
                if find(k) != root:
                    is_connected = False
                    break
            

            if is_connected and check_degree(tree_edges, d):
                return tree_edges
        return None

    result = find_spanning_tree(edges, n, d)

    if result:
        print("YES")
        for u, v in result:
            print(u, v)
    else:
        print("NO")

solve()