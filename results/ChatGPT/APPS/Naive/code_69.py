def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Start with vertex 1
    if len(graph[1]) < D:
        print("NO")
        return
    
    # We will store the edges of the spanning tree
    spanning_tree_edges = []
    visited = [False] * (n + 1)
    
    # Start BFS or DFS from vertex 1
    queue = deque([1])
    visited[1] = True
    degree_count = 0
    
    # Use a list to track the children of vertex 1
    children = []
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                
                # If we are adding edges from vertex 1, track them
                if current == 1 and degree_count < D:
                    spanning_tree_edges.append((1, neighbor))
                    children.append(neighbor)
                    degree_count += 1
                elif current != 1:
                    spanning_tree_edges.append((current, neighbor))
    
    # If we did not reach the required degree for vertex 1
    if degree_count < D:
        print("NO")
        return
    
    # Ensure the spanning tree is valid (n-1 edges)
    if len(spanning_tree_edges) != n - 1:
        print("NO")
        return
    
    print("YES")
    for u, v in spanning_tree_edges:
        print(u, v)

# Example usage:
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)