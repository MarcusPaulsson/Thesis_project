def can_form_keyboard(s):
    from collections import defaultdict, deque
    
    # Create a graph to represent adjacent characters
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

    # Check for any characters with degree > 2 (which means it can't be a linear layout)
    for d in degree.values():
        if d > 2:
            return "NO", ""
    
    # Find the starting point (a character with degree 1 or any character if all have degree 2)
    start = None
    for char in degree:
        if degree[char] == 1:
            start = char
            break
    if start is None:
        start = next(iter(degree))  # Just take any character

    # Perform BFS or DFS to get the order of characters
    visited = set()
    layout = []
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        layout.append(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    # If we covered all characters
    if len(visited) < 26:
        layout = ''.join(layout) + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in visited)
    else:
        layout = ''.join(layout)

    return "YES", layout


# Input handling
T = int(input())
results = []
for _ in range(T):
    s = input().strip()
    result = can_form_keyboard(s)
    results.append(result)

# Output results
for res in results:
    if res[0] == "NO":
        print("NO")
    else:
        print("YES")
        print(res[1])