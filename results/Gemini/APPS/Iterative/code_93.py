def solve():
    n, d, k = map(int, input().split())

    if d >= n:
        print("NO")
        return

    if d == 1 and n > 2:
        if k <= 1:
            print("NO")
            return
    elif k == 1 and d > 1:
        print("NO")
        return
    elif k == 1 and d ==1 and n > 2:
        print("NO")
        return
    elif n == 1 and d == 0:
        print("YES")
        return
        

    edges = []
    nodes = [[] for _ in range(n + 1)]

    # Create the diameter path
    for i in range(1, d + 1):
        edges.append((i, i + 1))
        nodes[i].append(i + 1)
        nodes[i + 1].append(i)

    # Check if possible to add more nodes
    if d + 1 > n:
        print("NO")
        return

    next_node = d + 2
    for i in range(1, d + 2):
        while len(nodes[i]) < k and next_node <= n:
            edges.append((i, next_node))
            nodes[i].append(next_node)
            nodes[next_node].append(i)
            next_node += 1

    if next_node <= n:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)

solve()