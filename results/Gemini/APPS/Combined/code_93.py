def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if k == 1:
        if d > 1 or n > d + 1:
            print("NO")
            return
        else:
            print("YES")
            for i in range(d):
                print(i + 1, i + 2)
            return

    if d > n - 1:
        print("NO")
        return

    if d == 1 and n > 2 and k < 2:
        print("NO")
        return
    
    if d == 1 and n > k + 1:
        print("NO")
        return

    edges = []
    degrees = [0] * (n + 1)

    # Create a path of length d
    for i in range(d):
        edges.append((i + 1, i + 2))
        degrees[i + 1] += 1
        degrees[i + 2] += 1

    next_node = d + 2

    # Add remaining nodes to the path
    for i in range(1, d + 2):
        while degrees[i] < k and next_node <= n:
            edges.append((i, next_node))
            degrees[i] += 1
            degrees[next_node] += 1
            next_node += 1

    if next_node <= n:
        print("NO")
        return

    if len(edges) != n - 1:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()