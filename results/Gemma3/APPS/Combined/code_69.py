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
        
        # First, add edges connected to vertex 1 until its degree is D
        degree_one = 0
        for u, v in edges:
            if u == 1 or v == 1:
                if union(u, v):
                    selected_edges.append((u, v))
                    if u == 1 or v == 1:
                        degree_one += 1
                    if degree_one == target_degree:
                        break
        
        if degree_one != target_degree:
            return None
        
        # Then, add the remaining edges to form a spanning tree
        for u, v in edges:
            if union(u, v):
                selected_edges.append((u, v))
        
        # Check if it's a spanning tree
        num_edges = len(selected_edges)
        if num_edges != n - 1:
            return None
        
        return selected_edges
    
    spanning_tree = find_spanning_tree(d)
    
    if spanning_tree is None:
        print("NO")
    else:
        print("YES")
        for u, v in spanning_tree:
            print(u, v)

solve()