def dfs(node, parent, depth, graph, depths, farthest):
    depths[node] = depth
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, graph, depths, farthest)
            if depths[neighbor] > depths[farthest[0]]:
                farthest[0] = neighbor

def find_farthest(node, graph):
    depths = [-1] * len(graph)
    farthest = [node]
    dfs(node, -1, 0, graph, depths, farthest)
    return farthest[0], depths

def get_edges_count(a, b, c, parent, graph):
    path_edges = set()
    def add_path_edges(start, end):
        while start != end:
            path_edges.add((min(start, parent[start]), max(start, parent[start])))
            start = parent[start]
    
    add_path_edges(a, b)
    add_path_edges(b, c)
    add_path_edges(a, c)
    
    return len(path_edges)

def main():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    graph = defaultdict(list)
    
    for line in data[1:n]:
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 1: Find two farthest points in the tree
    first_farthest, _ = find_farthest(1, graph)
    second_farthest, depths = find_farthest(first_farthest, graph)
    
    # Step 2: Get parent information for the path
    parent = [-1] * (n + 1)
    stack = [(first_farthest, -1)]
    while stack:
        node, par = stack.pop()
        parent[node] = par
        for neighbor in graph[node]:
            if neighbor != par:
                stack.append((neighbor, node))

    # Step 3: Get the farthest point from the second farthest to get all edges
    third_farthest, _ = find_farthest(second_farthest, graph)
    
    # Step 4: Calculate edges
    result_edges = get_edges_count(first_farthest, second_farthest, third_farthest, parent, graph)
    
    print(result_edges)
    print(first_farthest, second_farthest, third_farthest)

if __name__ == "__main__":
    main()