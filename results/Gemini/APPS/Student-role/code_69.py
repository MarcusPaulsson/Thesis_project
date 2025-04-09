def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    def build_spanning_tree(edges, n, d):
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def check_degree(tree_edges, d):
            degree = 0
            for u, v in tree_edges:
                if u == 1 or v == 1:
                    degree += 1
            return degree == d

        def is_connected(tree_edges, n):
            if not tree_edges:
                return False if n > 1 else True
            
            adj_list = [[] for _ in range(n + 1)]
            for u, v in tree_edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            
            visited = [False] * (n + 1)
            
            def dfs(node):
                visited[node] = True
                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        dfs(neighbor)
            
            dfs(1)
            for i in range(1, n + 1):
                if not visited[i]:
                    return False
            return True

        def find_spanning_tree(index, current_tree_edges):
            if len(current_tree_edges) == n - 1:
                if check_degree(current_tree_edges, d) and is_connected(current_tree_edges, n):
                    return current_tree_edges
                else:
                    return None
            
            if index == len(edges):
                return None
            
            # Option 1: Include the current edge in the spanning tree
            new_tree_edges = current_tree_edges + [edges[index]]
            result = find_spanning_tree(index + 1, new_tree_edges)
            if result:
                return result
            
            # Option 2: Exclude the current edge from the spanning tree
            result = find_spanning_tree(index + 1, current_tree_edges)
            if result:
                return result
            
            return None

        spanning_tree = find_spanning_tree(0, [])
        return spanning_tree

    spanning_tree = build_spanning_tree(edges, n, d)

    if spanning_tree:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)
    else:
        print("NO")

solve()