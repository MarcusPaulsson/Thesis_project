def dfs(node, parent, depth):
    farthest_node = (depth, node)
    for neighbor in tree[node]:
        if neighbor != parent:
            farthest_node = max(farthest_node, dfs(neighbor, node, depth + 1))
    return farthest_node

def find_farthest(node):
    return dfs(node, -1, 0)

def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    global tree
    tree = defaultdict(list)

    for i in range(1, n):
        u, v = map(int, data[i].split())
        tree[u].append(v)
        tree[v].append(u)

    # Step 1: Find the farthest node from an arbitrary start point (1)
    _, farthest_from_start = find_farthest(1)

    # Step 2: Find the farthest node from the previously found farthest node
    _, farthest_from_far = find_farthest(farthest_from_start)

    # Step 3: Find the path from farthest_from_start to farthest_from_far to get the diameter
    diameter_path = []
    def find_path(node, parent, target):
        if node == target:
            return True
        for neighbor in tree[node]:
            if neighbor != parent and find_path(neighbor, node, target):
                diameter_path.append(neighbor)
                return True
        return False

    find_path(farthest_from_start, -1, farthest_from_far)
    diameter_path.append(farthest_from_start)

    # The diameter path will have all nodes in the longest path in the tree
    if len(diameter_path) < 3:
        print(n - 1)
        print(1, 2, 3)
        return

    a = diameter_path[0]
    b = diameter_path[len(diameter_path) - 1]

    # To maximize edges, we can pick two end points of the diameter and a leaf node
    leaf_node = -1
    for neighbor in tree[a]:
        if neighbor != b:
            leaf_node = neighbor
            break
    
    if leaf_node == -1:
        for neighbor in tree[b]:
            if neighbor != a:
                leaf_node = neighbor
                break

    print(len(diameter_path) - 1 + len(tree[leaf_node]))
    print(a, b, leaf_node)

if __name__ == "__main__":
    main()