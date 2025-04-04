from collections import defaultdict, deque

def bfs(start, graph):
    queue = deque([start])
    visited = {start: 0}
    farthest_node = start

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
                if visited[neighbor] > visited[farthest_node]:
                    farthest_node = neighbor

    return farthest_node, visited

def find_max_edges(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Step 1: Find the farthest node from an arbitrary node (node 1)
    farthest_node, _ = bfs(1, graph)

    # Step 2: Find the farthest node from the found farthest node
    opposite_node, distances = bfs(farthest_node, graph)

    # Step 3: Find the diameter of the tree
    diameter_length = distances[opposite_node]

    # Step 4: Construct the path from farthest_node to opposite_node
    path_nodes = []
    current = opposite_node
    while current != farthest_node:
        path_nodes.append(current)
        for neighbor in graph[current]:
            if distances[neighbor] == distances[current] - 1:
                current = neighbor
                break

    path_nodes.append(farthest_node)
    path_nodes.reverse()

    # Choose the endpoints of the longest path and one of their neighbors
    a = path_nodes[0]
    b = path_nodes[-1]
    c = path_nodes[len(path_nodes) // 2]

    return diameter_length + 1, a, b, c

def main():
    n = int(input("Enter the number of nodes: "))
    if n < 2:
        print("The number of nodes must be at least 2.")
        return
    
    edges = [tuple(map(int, input("Enter edge (u v): ").split())) for _ in range(n - 1)]
    result, a, b, c = find_max_edges(n, edges)
    print(result)
    print(a, b, c)

if __name__ == "__main__":
    main()