def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    def find_spanning_tree(target_degree):
        
        def dfs(node, visited, current_tree):
            visited[node] = True
            for u, v in edges:
                neighbor = None
                if u == node and not visited[v]:
                    neighbor = v
                elif v == node and not visited[u]:
                    neighbor = u
                
                if neighbor is not None:
                    current_tree.append((node, neighbor))
                    dfs(neighbor, visited, current_tree)
        
        
        for start_node in [1]:
            visited = [False] * (n + 1)
            current_tree = []
            dfs(start_node, visited, current_tree)
            
            if len(current_tree) != n - 1:
                continue
            
            degree = 0
            for u, v in current_tree:
                if u == 1 or v == 1:
                    degree += 1
            
            if degree == target_degree:
                return current_tree
        
        return None

    spanning_tree = find_spanning_tree(d)
    
    if spanning_tree is None:
        print("NO")
    else:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)

solve()