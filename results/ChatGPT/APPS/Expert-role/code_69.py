def find_spanning_tree(n, m, D, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    if len(graph[1]) < D:
        print("NO")
        return

    # Start with vertex 1 and try to build the spanning tree
    chosen_edges = []
    degree_count = {i: 0 for i in range(1, n + 1)}
    degree_count[1] = 0

    # Select D edges from vertex 1
    for neighbor in graph[1][:D]:
        chosen_edges.append((1, neighbor))
        degree_count[1] += 1
        degree_count[neighbor] += 1

    # Now we need to add edges for the remaining vertices to connect them
    visited = set([1] + [neighbor for neighbor in graph[1][:D]])
    queue = deque()

    # Add remaining neighbors of vertex 1 to the queue to explore
    for neighbor in graph[1][D:]:
        if degree_count[neighbor] == 0:
            queue.append(neighbor)

    for i in range(2, n + 1):
        if i not in visited:
            queue.append(i)

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if degree_count[neighbor] < 1 and neighbor not in visited:
                chosen_edges.append((current, neighbor))
                degree_count[current] += 1
                degree_count[neighbor] += 1
                visited.add(neighbor)
                if len(chosen_edges) == n - 1:
                    break
        if len(chosen_edges) == n - 1:
            break

    if len(chosen_edges) != n - 1:
        print("NO")
    else:
        print("YES")
        for u, v in chosen_edges:
            print(u, v)

# Example usage:
n, m, D = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_spanning_tree(n, m, D, edges)