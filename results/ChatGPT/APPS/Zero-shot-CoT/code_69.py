def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Create adjacency list
    graph = defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)
    
    # If D is greater than the number of edges connected to vertex 1, return NO
    if D > len(graph[1]):
        return "NO"
    
    # Start forming the spanning tree
    selected_edges = []
    visited = set()
    visited.add(1)
    
    # First, we want to pick D edges from vertex 1
    degree_count = 0
    for neighbor in graph[1]:
        if degree_count < D:
            selected_edges.append((1, neighbor))
            visited.add(neighbor)
            degree_count += 1
        else:
            break
    
    if degree_count < D:
        return "NO"
    
    # Use BFS/DFS to add the remaining edges
    queue = deque()
    queue.append(1)
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                selected_edges.append((current, neighbor))
                visited.add(neighbor)
                queue.append(neighbor)
                if len(selected_edges) == n - 1:
                    break

    # Check if we have exactly n-1 edges
    if len(selected_edges) != n - 1:
        return "NO"

    # Return the result
    result = ["YES"]
    result.extend(f"{v} {u}" for v, u in selected_edges)
    return "\n".join(result)

# Input reading
n, m, D = map(int, input().strip().split())
edges = [tuple(map(int, input().strip().split())) for _ in range(m)]

# Execute the function and print the result
print(find_spanning_tree(n, m, D, edges))