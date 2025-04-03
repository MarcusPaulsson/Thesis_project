def find_keyboard_layout(test_cases):
    results = []
    
    for s in test_cases:
        adjacency_list = {chr(i): set() for i in range(ord('a'), ord('z') + 1)}
        seen = set()
        
        for i in range(len(s) - 1):
            u, v = s[i], s[i + 1]
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)
            seen.add(u)
            seen.add(v)

        # Check for cycles and create a layout if possible
        visited = set()
        order = []
        is_possible = True
        
        def dfs(node, parent):
            nonlocal is_possible
            visited.add(node)
            order.append(node)
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    is_possible = False
                    return
                dfs(neighbor, node)
        
        for char in seen:
            if char not in visited:
                dfs(char, None)
                if not is_possible:
                    break
        
        if not is_possible or len(seen) < len(order):
            results.append("NO")
            continue
        
        remaining = set(chr(i) for i in range(ord('a'), ord('z') + 1)) - seen
        layout = ''.join(order) + ''.join(sorted(remaining))
        results.append("YES")
        results.append(layout)

    return results


# Reading input
T = int(input())
test_cases = [input().strip() for _ in range(T)]

# Getting the results
results = find_keyboard_layout(test_cases)

# Printing results
for result in results:
    print(result)