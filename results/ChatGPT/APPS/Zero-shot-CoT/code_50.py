from collections import defaultdict, deque

def bfs(start, n, tree):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farthest_node = start

    while q:
        node = q.popleft()
        for neighbor in tree[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                if dist[neighbor] > dist[farthest_node]:
                    farthest_node = neighbor
    return farthest_node, dist

def main():
    n = int(input())
    tree = defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    # First BFS to find the farthest node from an arbitrary node
    farthest_node_from_start, _ = bfs(1, n, tree)
    
    # Second BFS to find the farthest node from the previously found node
    farthest_node, dist_from_first = bfs(farthest_node_from_start, n, tree)

    # Get distances and find the maximum distance
    _, dist_from_second = bfs(farthest_node, n, tree)

    # Find two nodes which are farthest apart
    max_distance = 0
    a, b = -1, -1
    for i in range(1, n + 1):
        if dist_from_first[i] + dist_from_second[i] > max_distance:
            max_distance = dist_from_first[i] + dist_from_second[i]
            a, b = farthest_node_from_start, i

    # Find the third node which is not a or b
    c = -1
    for i in range(1, n + 1):
        if i != a and i != b:
            c = i
            break

    print(max_distance + 1)
    print(a, b, c)

if __name__ == "__main__":
    main()