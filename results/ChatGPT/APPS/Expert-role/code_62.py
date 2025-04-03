def perfect_keyboard(test_cases):
    results = []
    
    for s in test_cases:
        adjacency = {}
        for i in range(len(s) - 1):
            if s[i] not in adjacency:
                adjacency[s[i]] = set()
            if s[i + 1] not in adjacency:
                adjacency[s[i + 1]] = set()
            adjacency[s[i]].add(s[i + 1])
            adjacency[s[i + 1]].add(s[i])

        visited = {}
        layout = []

        def dfs(node):
            if node in visited:
                return
            visited[node] = True
            layout.append(node)
            for neighbor in adjacency[node]:
                dfs(neighbor)

        for char in adjacency.keys():
            if char not in visited:
                dfs(char)

        if len(visited) < len(adjacency):
            results.append("NO")
            continue

        remaining_chars = set("abcdefghijklmnopqrstuvwxyz") - set(layout)
        layout.extend(remaining_chars)
        results.append("YES")
        results.append("".join(layout))

    return results

# Input reading
T = int(input())
test_cases = [input().strip() for _ in range(T)]
results = perfect_keyboard(test_cases)

# Output results
for result in results:
    print(result)