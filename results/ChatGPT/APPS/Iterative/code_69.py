def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque
    
    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Check if it's possible to have the degree of vertex 1 equal to D
    if len(graph[1]) < D:
        print("NO")
        return

    # Collect the edges of the spanning tree
    spanning_tree_edges = []
    degree_count = {i: 0 for i in range(1, n + 1)}
    
    # Start the spanning tree construction
    queue = deque([1])
    degree_count[1] = 0  # Start with vertex 1
    used = {1}  # Track used vertices

    while queue:
        current = queue.popleft()
        
        # Stop if vertex 1 has reached the desired degree
        if current == 1 and degree_count[1] == D:
            continue
        
        for neighbor in graph[current]:
            # Only consider edges that do not exceed the required degree for vertex 1
            if degree_count[current] < (D if current == 1 else n - 1) and degree_count[neighbor] < n - 1:
                spanning_tree_edges.append((current, neighbor))
                degree_count[current] += 1
                degree_count[neighbor] += 1
                
                if neighbor != 1 and neighbor not in used:
                    queue.append(neighbor)
                    used.add(neighbor)
                
                # If we reached the required degree for vertex 1, we can stop
                if current == 1 and degree_count[1] == D:
                    break

    # Check if we have used n-1 edges and degree of vertex 1 is D
    if len(spanning_tree_edges) == n - 1 and degree_count[1] == D:
        print("YES")
        for u, v in spanning_tree_edges:
            print(u, v)
    else:
        print("NO")


# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()
n, m, D = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Call the function
find_spanning_tree(n, m, D, edges)