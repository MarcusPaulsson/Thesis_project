def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        print("NO")
        return

    if k == 1 and d > 1:
        print("NO")
        return
    
    if k == 1 and d == 1 and n > 2:
        print("NO")
        return

    edges = []
    nodes = list(range(1, n + 1))

    # Create the diameter path
    for i in range(d):
        edges.append((i + 1, i + 2))

    used_nodes = set(range(1, d + 2))
    
    if len(used_nodes) > n:
        print("NO")
        return

    remaining_nodes = [node for node in nodes if node not in used_nodes]

    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    # Add remaining nodes to the diameter path
    for node in remaining_nodes:
        found_parent = False
        for i in range(1, d + 2):
            if degrees[i] < k:
                edges.append((node, i))
                degrees[node] += 1
                degrees[i] += 1
                found_parent = True
                break
        if not found_parent:
            print("NO")
            return

    # Check if all nodes are connected and degrees are valid
    if len(edges) != n - 1:
        print("NO")
        return

    for i in range(1, n + 1):
        if degrees[i] > k:
            print("NO")
            return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()