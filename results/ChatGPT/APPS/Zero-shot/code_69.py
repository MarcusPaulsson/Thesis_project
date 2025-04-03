def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check if the degree D is possible (not exceeding the maximum degree of vertex 1)
    if len(graph[1]) < D:
        return "NO"
    
    # Prepare for BFS/DFS to build the spanning tree
    visited = [False] * (n + 1)
    visited[1] = True
    spanning_tree_edges = []
    
    # Start from vertex 1
    degree_count = 0
    queue = deque([1])
    
    while queue and len(spanning_tree_edges) < n - 1:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                if current == 1 and degree_count < D:
                    # Allow vertex 1 to connect to D neighbors
                    spanning_tree_edges.append((current, neighbor))
                    visited[neighbor] = True
                    queue.append(neighbor)
                    degree_count += 1
                elif current != 1:
                    # Any other vertex can connect to any unvisited neighbor
                    spanning_tree_edges.append((current, neighbor))
                    visited[neighbor] = True
                    queue.append(neighbor)
                
                # Stop if we have enough edges
                if len(spanning_tree_edges) == n - 1:
                    break
    
    # Check if we have a spanning tree of size n-1
    if len(spanning_tree_edges) != n - 1 or degree_count != D:
        return "NO"
    
    result = ["YES"]
    result.extend(f"{u} {v}" for u, v in spanning_tree_edges)
    
    return "\n".join(result)

# Input reading
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Get the result
result = find_spanning_tree(n, m, D, edges)

# Print the result
print(result)