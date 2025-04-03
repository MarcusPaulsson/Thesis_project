def can_form_keyboard(s):
    from collections import defaultdict, deque

    # Create an adjacency list and a degree count for each character
    graph = defaultdict(set)
    degree = defaultdict(int)

    # Build the graph based on adjacent characters in the string
    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        if b not in graph[a]:
            graph[a].add(b)
            graph[b].add(a)
            degree[a] += 1
            degree[b] += 1

    # Check for vertices with degree > 2
    if any(deg > 2 for deg in degree.values()):
        return "NO", ""

    # Perform a BFS/DFS to create the layout
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from any character with degree 1 or any character that exists
    for char in degree:
        if char not in visited:
            dfs(char)

    # Fill in the remaining characters which are not in the password
    all_chars = set(chr(i) for i in range(ord('a'), ord('z') + 1))
    remaining_chars = all_chars - set(order)
    order.extend(sorted(remaining_chars))

    return "YES", ''.join(order)

# Read input
T = int(input())
for _ in range(T):
    s = input().strip()
    result, layout = can_form_keyboard(s)
    if result == "NO":
        print(result)
    else:
        print(result)
        print(layout)