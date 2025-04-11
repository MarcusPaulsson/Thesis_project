def solve():
    n, m, d = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    def find_spanning_tree(target_degree):
        parent = [0] * (n + 1)
        rank = [0] * (n + 1)
        
        def find(i):
            if parent[i] == 0:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False
        
        selected_edges = []
        
        # First, try to connect the first vertex to D other vertices
        count = 0
        for u, v in edges:
            if u == 1:
                if union(u, v):
                    selected_edges.append((u, v))
                    count += 1
                if count == target_degree:
                    break
        
        # If we couldn't connect the first vertex to D other vertices, return None
        if count != target_degree:
            return None
        
        # Then, add the remaining edges to form a spanning tree
        for u, v in edges:
            if (u, v) not in selected_edges and (v, u) not in selected_edges:
                if union(u, v):
                    selected_edges.append((u, v))
        
        # Check if we have a spanning tree
        num_components = 0
        for i in range(1, n + 1):
            if parent[i] == 0:
                num_components += 1
                find(i)
        
        if num_components == 1:
            return selected_edges
        else:
            return None
    
    spanning_tree = find_spanning_tree(d)
    
    if spanning_tree is None:
        print("NO")
    else:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)

solve()